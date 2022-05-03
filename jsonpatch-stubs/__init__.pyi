# -*- coding: utf-8 -*-

import typing
from collections.abc import Generator
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypedDict,
    TypeVar,
    Union
)

from _typeshed import Incomplete

import jsonpointer

_K = TypeVar("_K")
_K_contra = TypeVar("_K_contra", contravariant=True)
_V = TypeVar("_V")
_V_co = TypeVar("_V_co", covariant=True)
_T = TypeVar("_T")
RFC6902_OPERATIONS = Literal["add", "remove", "replace", "move", "copy", "test"]
RFC6902_OPERATION_OBJECT_BASE = TypedDict(
    "RFC6902_OPERATION_OBJECT_BASE",
    {
        "op": RFC6902_OPERATIONS,
        "path": str,
    }
)
RFC6902_OPERATION_OBJECT_ADD = TypedDict(
    "RFC6902_OPERATION_OBJECT_ADD",
    {
        "op": Literal["add"],
        "path": str,
        "value": Any
    }
)
RFC6902_OPERATION_OBJECT_REMOVE = TypedDict(
    "RFC6902_OPERATION_OBJECT_REMOVE",
    {
        "op": Literal["remove"],
        "path": str
    }
)
RFC6902_OPERATION_OBJECT_REPLACE = TypedDict(
    "RFC6902_OPERATION_OBJECT_REPLACE",
    {
        "op": Literal["replace"],
        "path": str,
        "value": Any
    }
)
RFC6902_OPERATION_OBJECT_MOVE = TypedDict(
    "RFC6902_OPERATION_OBJECT_MOVE",
    {
        "op": Literal["move"],
        "path": str,
        "from": str
    }
)
RFC6902_OPERATION_OBJECT_COPY = TypedDict(
    "RFC6902_OPERATION_OBJECT_COPY",
    {
        "op": Literal["copy"],
        "path": str,
        "from": str
    }
)
RFC6902_OPERATION_OBJECT_TEST = TypedDict(
    "RFC6902_OPERATION_OBJECT_TEST",
    {
        "op": Literal["test"],
        "path": str,
        "value": Any
    }
)
RFC6902_OPERATION_OBJECT = Union[
    RFC6902_OPERATION_OBJECT_ADD,
    RFC6902_OPERATION_OBJECT_REMOVE,
    RFC6902_OPERATION_OBJECT_REPLACE,
    RFC6902_OPERATION_OBJECT_MOVE,
    RFC6902_OPERATION_OBJECT_COPY,
    RFC6902_OPERATION_OBJECT_TEST,
]
_JSONPOINTER = Type[jsonpointer.JsonPointer]
class INDEXABLE(typing.Protocol[_K_contra, _V_co]):
    def __getitem__(self, index: _K_contra) -> _V_co: ...
_JSON_OBJECT_KEY = str
_JSON_OBJECT = Mapping[_JSON_OBJECT_KEY, "_JSON_VALUE"]
_JSON_ARRAY = Sequence["_JSON_VALUE"]
_JSON_VALUE = Union[str, complex, _JSON_OBJECT, _JSON_ARRAY, bool, None]
_JSONPOINTER_SUPPORTED_VALUES = Union[
    _JSON_VALUE,
    Mapping[_JSON_OBJECT_KEY, "_JSONPOINTER_SUPPORTED_VALUES"],
    Sequence["_JSONPOINTER_SUPPORTED_VALUES"],
    INDEXABLE[_JSON_OBJECT_KEY, "_JSONPOINTER_SUPPORTED_VALUES"],
]
_JSONPOINTER_SUPPORTED_ROOT_VALUES = Union[
    Mapping[_JSON_OBJECT_KEY, "_JSONPOINTER_SUPPORTED_VALUES"],
    Sequence["_JSONPOINTER_SUPPORTED_VALUES"],
    INDEXABLE[_JSON_OBJECT_KEY, "_JSONPOINTER_SUPPORTED_VALUES"],
]
_JSON__LOADS = Callable[[Union[str, bytes, bytearray]], _JSON_VALUE]
_JSON__DUMPS = Callable[[_JSON_VALUE], str]
_T_JSONPOINTER_SUPPORTED_ROOT_VALUES = TypeVar(
    "_T_JSONPOINTER_SUPPORTED_ROOT_VALUES",
    Mapping[_JSON_OBJECT_KEY, "_JSONPOINTER_SUPPORTED_VALUES"],
    Sequence["_JSONPOINTER_SUPPORTED_VALUES"],
    INDEXABLE[_JSON_OBJECT_KEY, "_JSONPOINTER_SUPPORTED_VALUES"],
)

class JsonPatchException(Exception): ...
class InvalidJsonPatch(JsonPatchException): ...
class JsonPatchConflict(JsonPatchException): ...
class JsonPatchTestFailed(JsonPatchException, AssertionError): ...

def multidict(
    ordered_pairs: Iterable[Tuple[_K, _V]]
) -> Dict[_K, Union[_V, List[_V]]]: ...
def apply_patch(
    doc: _JSONPOINTER_SUPPORTED_ROOT_VALUES,
    patch: Union[Sequence[RFC6902_OPERATION_OBJECT], Union[str, bytes]],
    in_place: bool = ...,
    pointer_cls: Optional[_JSONPOINTER] = ...,
): ...
def make_patch(
    src: _JSONPOINTER_SUPPORTED_VALUES,
    dst: _JSONPOINTER_SUPPORTED_VALUES,
    pointer_cls: Optional[_JSONPOINTER] = ...,
): ...

class PatchOperation:
    pointer_cls: Optional[_JSONPOINTER]
    location: str
    pointer: _JSONPOINTER
    operation: RFC6902_OPERATION_OBJECT
    def __init__(
        self,
        operation: RFC6902_OPERATION_OBJECT,
        pointer_cls: Optional[_JSONPOINTER] = ...,
    ) -> None: ...
    def apply(self, obj: _JSONPOINTER_SUPPORTED_ROOT_VALUES) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def path(self): ...
    @property
    def key(self): ...
    @key.setter
    def key(self, value) -> None: ...

class RemoveOperation(PatchOperation):
    def apply(self, obj: _JSONPOINTER_SUPPORTED_ROOT_VALUES): ...

class AddOperation(PatchOperation):
    def apply(self, obj: _JSONPOINTER_SUPPORTED_ROOT_VALUES): ...

class ReplaceOperation(PatchOperation):
    def apply(self, obj: _JSONPOINTER_SUPPORTED_ROOT_VALUES): ...

class MoveOperation(PatchOperation):
    def apply(self, obj: _JSONPOINTER_SUPPORTED_ROOT_VALUES): ...
    @property
    def from_path(self): ...
    @property
    def from_key(self): ...
    @from_key.setter
    def from_key(self, value) -> None: ...

class TestOperation(PatchOperation):
    def apply(self, obj: _JSONPOINTER_SUPPORTED_ROOT_VALUES): ...

class CopyOperation(PatchOperation):
    def apply(self, obj: _JSONPOINTER_SUPPORTED_ROOT_VALUES): ...

class JsonPatch:
    json_dumper: Incomplete
    json_loader: Incomplete
    operations: Incomplete
    patch: Sequence[RFC6902_OPERATION_OBJECT]
    pointer_cls: Optional[_JSONPOINTER]
    def __init__(
        self,
        patch: Sequence[RFC6902_OPERATION_OBJECT],
        pointer_cls: Optional[_JSONPOINTER] = ...,
    ) -> None: ...
    def __bool__(self): ...
    __nonzero__: Incomplete
    def __iter__(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @classmethod
    @typing.overload
    def from_string(
        cls,
        patch_str: Union[str, bytes, bytearray],
        loads: None = ...,
        pointer_cls: Optional[_JSONPOINTER] = ...,
    ) -> "JsonPatch": ...
    @classmethod
    @typing.overload
    def from_string(
        cls,
        patch_str: _T,
        loads: Callable[[_T], RFC6902_OPERATION_OBJECT] = ...,
        pointer_cls: Optional[_JSONPOINTER] = ...,
    ) -> "JsonPatch": ...
    @classmethod
    def from_diff(
        cls,
        src: _JSONPOINTER_SUPPORTED_VALUES,
        dst: _JSONPOINTER_SUPPORTED_VALUES,
        optimization: bool = ...,
        dumps: Optional[_JSON__DUMPS] = ...,
        pointer_cls: Optional[_JSONPOINTER] = ...,
    ) -> "JsonPatch": ...
    def to_string(self, dumps: Optional[_JSON__DUMPS] = ...) -> str: ...
    def apply(self, obj: _T_JSONPOINTER_SUPPORTED_ROOT_VALUES, in_place: bool = ...) -> _T_JSONPOINTER_SUPPORTED_ROOT_VALUES: ...

class DiffBuilder:
    dumps: Incomplete
    pointer_cls: Incomplete
    index_storage: Incomplete
    index_storage2: Incomplete
    src_doc: _JSONPOINTER_SUPPORTED_VALUES
    dst_doc: _JSONPOINTER_SUPPORTED_VALUES
    def __init__(
        self,
        src_doc: _JSONPOINTER_SUPPORTED_VALUES,
        dst_doc: _JSONPOINTER_SUPPORTED_VALUES,
        dumps: Optional[_JSON__DUMPS] = ...,
        pointer_cls: Optional[_JSONPOINTER] = ...,
    ) -> None: ...
    def store_index(self, value, index, st) -> None: ...
    def take_index(self, value, st): ...
    def insert(self, op): ...
    def remove(self, index) -> None: ...
    def iter_from(self, start) -> Generator[Incomplete, None, None]: ...
    def __iter__(self): ...
    def execute(self) -> Generator[Incomplete, None, None]: ...
