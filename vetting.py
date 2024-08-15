from interactions import Extension, Embed, OptionType, slash_option, Member
from interactions.ext.hybrid_commands import hybrid_slash_command, HybridContext

class VettingCommands(Extension):
    def __init__(self, bot):
        self.bot = bot

    @hybrid_slash_command(name="ban", description="This Ban Command Is For Unverified Users", scopes=[898568341499838514])
    @slash_option(
        name="user",
        description="User You Wish To Ban",
        opt_type=OptionType.USER,
        required=True
    )
    @slash_option(
        name="reason",
        description="Reason for the ban",
        opt_type=OptionType.STRING,
        required=True
    )
    async def bc_ban_function(self, ctx: HybridContext, user: Member, reason: str = None):
        border_clerk_role_id = 1031959498857910323
        if border_clerk_role_id not in [role.id for role in ctx.author.roles]:
            await ctx.send("You do not have permission to use this command.", ephemeral=True)
            return
        
        unverified_role_id = 789452150337568771
        if unverified_role_id in [role.id for role in user.roles]:
            await ctx.send("Cannot ban verified users.", ephemeral=True)
            return
        
        allowed_channel_id = 1130690335341826099
        if ctx.channel.id != allowed_channel_id:
            await ctx.send("This command can only be used in the Border Holding channel.", ephemeral=True)
            return

        try:
            await user.ban(reason=reason)
            # Send a message to the shared mod log channel
            mod_log_channel_id = 898569694779420683
            mod_log_channel = self.bot.get_channel(mod_log_channel_id)
            await mod_log_channel.send(f"{user.mention} was banned for: {reason}")
            await ctx.send("User banned successfully.", hidden=True)

        except Exception as e:
            await ctx.send(f"Failed to ban user: {e}", hidden=True)