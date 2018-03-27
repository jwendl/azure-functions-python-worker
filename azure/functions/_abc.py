import abc
import datetime
import io
import typing


T = typing.TypeVar('T')


class Out(abc.ABC, typing.Generic[T]):
    """An interface to set function output parameters."""

    @abc.abstractmethod
    def set(self, val: T) -> None:
        """Set the value of the output parameter."""
        pass

    @abc.abstractmethod
    def get(self) -> T:
        """Get the value of the output parameter."""
        pass


class Context(abc.ABC):
    """Function invocation context."""

    @property
    @abc.abstractmethod
    def invocation_id(self) -> str:
        """Function invocation ID."""
        pass

    @property
    @abc.abstractmethod
    def function_name(self) -> str:
        """Function name."""
        pass

    @property
    @abc.abstractmethod
    def function_directory(self) -> str:
        """Function directory."""
        pass


class HttpRequest(abc.ABC):
    """HTTP request object."""

    @property
    @abc.abstractmethod
    def method(self) -> str:
        """Request method."""
        pass

    @property
    @abc.abstractmethod
    def url(self) -> str:
        """Request URL."""
        pass

    @property
    @abc.abstractmethod
    def headers(self) -> typing.Mapping[str, str]:
        """A dictionary containing request headers."""
        pass

    @property
    @abc.abstractmethod
    def params(self) -> typing.Mapping[str, str]:
        """A dictionary containing request GET parameters."""
        pass

    @abc.abstractmethod
    def get_body(self) -> bytes:
        """Return request body as bytes."""
        pass

    @abc.abstractmethod
    def get_json(self) -> typing.Any:
        """Decode and return request body as JSON.

        :raises ValueError:
            when the request does not contain valid JSON data.
        """
        pass


class HttpResponse(abc.ABC):

    @property
    @abc.abstractmethod
    def status_code(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def mimetype(self):
        pass

    @property
    @abc.abstractmethod
    def charset(self):
        pass

    @property
    @abc.abstractmethod
    def headers(self) -> typing.MutableMapping[str, str]:
        pass

    @abc.abstractmethod
    def get_body(self) -> bytes:
        pass


class TimerRequest(abc.ABC):
    """Timer request object."""

    @property
    @abc.abstractmethod
    def past_due(self) -> bool:
        """Whether the timer is past due."""
        pass


class InputStream(io.BufferedIOBase, abc.ABC):
    """File-like object representing an input blob."""

    @abc.abstractmethod
    def read(self, size=-1) -> bytes:
        """Return and read up to *size* bytes.

        :param int size:
            The number of bytes to read.  If the argument is omitted,
            ``None``, or negative, data is read and returned until
            EOF is reached.

        :return:
            Bytes read from the input stream.
        """
        pass

    @property
    @abc.abstractmethod
    def name(self) -> typing.Optional[str]:
        """The name of the blob."""
        pass

    @property
    @abc.abstractmethod
    def length(self) -> typing.Optional[int]:
        """The size of the blob in bytes."""
        pass

    @property
    @abc.abstractmethod
    def uri(self) -> typing.Optional[str]:
        """The blob's primary location URI."""
        pass


class QueueMessage(abc.ABC):

    @property
    @abc.abstractmethod
    def id(self) -> typing.Optional[str]:
        pass

    @abc.abstractmethod
    def get_body(self) -> typing.Union[str, bytes]:
        pass

    @abc.abstractmethod
    def get_json(self) -> typing.Any:
        pass

    @property
    @abc.abstractmethod
    def dequeue_count(self) -> typing.Optional[int]:
        pass

    @property
    @abc.abstractmethod
    def expiration_time(self) -> typing.Optional[datetime.datetime]:
        pass

    @property
    @abc.abstractmethod
    def insertion_time(self) -> typing.Optional[datetime.datetime]:
        pass

    @property
    @abc.abstractmethod
    def next_visible_time(self) -> typing.Optional[datetime.datetime]:
        pass

    @property
    @abc.abstractmethod
    def pop_receipt(self) -> typing.Optional[str]:
        pass
