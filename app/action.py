from app.model import Request, Response
from app.routes import Action, installed_routes


def action(request: Request) -> Response:
    actionToExecute: Action | None = next(
        filter(lambda action: action.match(request), installed_routes), None
    )

    if actionToExecute is None:
        return Response.NotFound()

    return actionToExecute.action(request)
