from __future__ import annotations

from ... import t

if t.TYPE_CHECKING:
    type OkT[ValT] = tuple[ValT, int, t.Literal[False]]
    type ErrT = tuple[None, int, t.Literal[True]]
    type ResultT[ValT] = OkT[ValT] | ErrT


def Ok[ValT](val: ValT, index: int) -> OkT[ValT]:
    return (val, index, False)


def Err(index: int) -> ErrT:
    return (None, index, True)


def isOk[ValT](res: ResultT[ValT]) -> t.TypeIs[OkT[ValT]]:
    return not res[2]


def isErr(res: ResultT[t.Any]) -> t.TypeIs[ErrT]:
    return bool(res[2])
