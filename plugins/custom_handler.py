from inmanta.agent.handler import ResourceHandler, HandlerContext
from inmanta.resources import Resource, PurgeableResource

class CustomHandler(ResourceHandler):
    def _extract_fields(self, resource: Resource, excluded={'purged', 'purge_on_delete'}) -> dict:
        return {
            key: getattr(resource, key)
            for key in resource.__class__.fields
            if key not in excluded}

    def execute(self, ctx: HandlerContext, desired_resource: Resource, dry_run: bool = None) -> None:
        try:
            self.pre(ctx, desired_resource)
            assert isinstance(desired_resource, PurgeableResource)

            """
            Main functionality
            """

        finally:
            try:
                self.post(ctx, desired_resource)
            except Exception as e:
                ctx.exception(
                    "An error occurred after deployment of %(resource_id)s (exception: %(exception)s",
                    resource_id=desired_resource.id,
                    exception=repr(e),
                )
