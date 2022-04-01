import utils
import functions as func
from commands.base import Cmd

help_text = [
    [
        ("Użycie:", "<PREFIX><COMMAND> `@USER`"),
        ("Description:",
         "Przekazuje własność kanału dla wybranej osoby aby stała się Twórcą kanału "
         "Dzięki temu nowa osoba może używać komend takich jak ( `private`, `limit`, `name`...)."),
        ("Przykład:",
         "```<PREFIX><COMMAND> @pixaal```"),
    ]
]


async def execute(ctx, params):
    name = ' '.join(params).strip()
    guild = ctx['guild']
    author = ctx['message'].author
    vc = ctx['voice_channel']

    user = utils.get_user_in_channel(name, vc)

    if not user:
        return False, "Can't find any user in your channel with the name \"{}\".".format(name)
    if user.id == ctx['creator_id']:
        if user == author:
            return False, "Jesteś już twórcą kanału."
        else:
            return False, "{} is already the creator.".format(func.user_hash(user))

    result = await func.set_creator(guild, vc.id, user)
    return result, None


command = Cmd(
    execute=execute,
    help_text=help_text,
    params_required=1,
    admin_required=False,
    voice_required=True,
    creator_only=True,
)
