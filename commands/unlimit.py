from commands.base import Cmd

help_text = [
    [
<<<<<<< HEAD
        ("Sposób Użycia:", "<PREFIX><COMMAND>"),
        ("Opis:",
         "Zdejmuje z kanału limit osób które mogą dołączyć. "
         "Limit jest dziediczony z kanału głównego."),
=======
        ("Usage:", "<PREFIX><COMMAND>"),
        (
            "Description:",
            "Remove the user limit in your channel. Also removes any limit that may have been "
            "inherited from the primary channel.",
        ),
>>>>>>> 17698450c6f885ae3ee3dae059754ba72931adf6
    ]
]


async def execute(ctx, params):
    from commands import limit

    return await limit.command.execute(ctx, ["0"])


command = Cmd(
    execute=execute,
    help_text=help_text,
    params_required=0,
    admin_required=False,
    voice_required=True,
    creator_only=True,
)
