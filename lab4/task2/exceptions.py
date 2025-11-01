class HeadException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class ConstContainerEditingError(HeadException): ...


class GraphError(Exception): ...


class VertexNotFoundError(GraphError): ...


class EdgeNotFoundError(GraphError): ...
