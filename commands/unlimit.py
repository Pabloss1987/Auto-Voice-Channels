from commands.base import Cmd

help_text = [
    [
        ("Usage:", "<PREFIX><COMMAND>"),
        ("Description:",
         "Zdejmuje z kanału limit osób które mogą dołączyć. "
         "Limit jest dziediczony z kanału głównego."),
    ]
]


async def execute(ctx, params):
    from commands import limit
    return await limit.command.execute(ctx, ['0'])


command = Cmd(
    execute=execute,
    help_text=help_text,
    params_required=0,
    admin_required=False,
    voice_required=True,
    creator_only=True,
)
