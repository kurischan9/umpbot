import asyncio
from datetime import datetime
import sqlite3
import string
from interactions import Extension, listen, Embed
from interactions.api.events import MessageCreate, ChannelCreate, MessageUpdate, MemberAdd, MemberRemove, Component

# Vetting Ticket Tracker (Checks If Questions Completed)
def initialize_database():
    conn = sqlite3.connect('bot_state.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS channel_states
                 (channel_id INTEGER PRIMARY KEY, completed BOOLEAN)''')
    print("Database initialized and table created.")
    conn.commit()
    conn.close()
def save_channel_state(channel_id, completed):
    conn = sqlite3.connect('bot_state.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO channel_states VALUES (?, ?)", (channel_id, completed))
    conn.commit()
    print(f"Saved state for channel {channel_id} as {completed}")
    conn.close()
def load_channel_states():
    conn = sqlite3.connect('bot_state.db')
    c = conn.cursor()
    c.execute("SELECT * FROM channel_states")
    rows = c.fetchall()
    conn.close()
    return dict((row[0], row[1]) for row in rows)
initialize_database()

class Listeners(Extension):
    def __init__(self, bot):
        self.bot = bot

    @listen(MessageCreate)
    async def message_create_handler(self, event: MessageCreate):
        # Ignore Bot Messages
        if event.message.author.bot:
            return
        
        # Checking The Category Where The Message Was Created
        # Vetting
        if event.message.channel.parent_id == 1130507431013789746:
            # Vetting
            # Learning
            # Extracting the username from the channel name
            channel_name_parts = event.message.channel.name.split('-')
            if channel_name_parts[0] == "learning":
                target_username = channel_name_parts[2].split('_')[0]  # Assuming the username does not contain underscores
                
                # Remove punctuation and underscores from the target_username
                target_username_clean = ''.join(ch for ch in target_username if ch not in string.punctuation and ch != '_')
                print(target_username_clean)
                
                # Check if the author's username matches the extracted username (after removing punctuation and underscores)
                author_username_clean = ''.join(ch for ch in event.message.author.username if ch not in string.punctuation and ch != '_')
                print(author_username_clean)  # Debugging print statement

                if author_username_clean != target_username_clean:
                    return # Not the right author
        
                recent_messages = await event.message.channel.fetch_messages(20)
                cap = sum(1 for msg in recent_messages)
                count = sum(1 for msg in recent_messages if msg._author_id == self.bot.user.id)
                
                channel_states = load_channel_states()
                if event.message.channel.id not in channel_states or not channel_states[event.message.channel.id]:
                    if cap <= 20:
                        if count <= 8:
                            embed_name = f"learning_question_{count + 1}"
                            embed_object = globals()[embed_name]
                            await event.message.channel.send(embed=embed_object)

                        if count == 9:
                            role_mention = f'<@&{1031959498857910323}>'
                            await event.message.channel.send(f"Thank You For Answering! {role_mention} Will Be With You Shortly.")
                            save_channel_state(event.message.channel.id, True)
            
            # Educated
            # Extracting the username from the channel name
            elif channel_name_parts[0] == "educated":
                target_username = channel_name_parts[2].split('_')[0]  # Assuming the username does not contain underscores
                
                # Remove punctuation and underscores from the target_username
                target_username_clean = ''.join(ch for ch in target_username if ch not in string.punctuation and ch != '_')
                print(target_username_clean)
                
                # Check if the author's username matches the extracted username (after removing punctuation and underscores)
                author_username_clean = ''.join(ch for ch in event.message.author.username if ch not in string.punctuation and ch != '_')
                print(author_username_clean)  # Debugging print statement

                if author_username_clean != target_username_clean:
                    return # Not the right author
        
                recent_messages = await event.message.channel.fetch_messages(50)
                cap = sum(1 for msg in recent_messages)
                print(cap)
                count = sum(1 for msg in recent_messages if msg._author_id == self.bot.user.id)
                
                channel_states = load_channel_states()
                if event.message.channel.id not in channel_states or not channel_states[event.message.channel.id]:
                    if cap <= 30:
                        if count <= 12:
                            embed_name = f"educated_question_{count + 1}"
                            embed_object = globals()[embed_name]
                            await event.message.channel.send(embed=embed_object)

                        if count == 13:
                            role_mention = f'<@&{986725357338116216}>'
                            await event.message.channel.send(f"Thank You For Answering! {role_mention} Will Be With You Shortly.")
                            save_channel_state(event.message.channel.id, True)
            
            else:
                return
                    
        
    @listen(ChannelCreate)
    async def channel_create_handler(self, event: ChannelCreate):
        # Checking The Channel
        new_channel = event.channel

        # Vetting
        # Checking If It Occured In Vetting Tickets
        if new_channel.parent_id == 1130507431013789746:
            await asyncio.sleep(1)
            channel_name_parts = event.channel.name.split('-')

            if channel_name_parts[0] == "learning":
                question_1 = Embed(
                title="[1 / 9] Why Do You Want To Join The Server?",
                description="Make sure you have read our discussion ethics to understand the level of discussion, and type of space we are building in the United Marxist Pact.",
                color="#2986cc"
                )
                await new_channel.send(embeds=[question_1])

            if channel_name_parts[0] == "educated":
                question_1 = Embed(
                title="[1 / 13] Why Do You Want To Join The Server?",
                description="Make sure you have read our discussion ethics to understand the level of discussion, and type of space we are building in the United Marxist Pact.",
                color="#2986cc"
                )
                await new_channel.send(embeds=[question_1])
        
        # Logging

    @listen(MessageUpdate)
    async def message_update_handler(self, event: MessageUpdate):
        # Ignore Bot Messages
        if event.after.author.bot:
            return
        
        if event.before.content == event.after.content:
            return
        
        # Logging
        old_message_content = event.before.content
        new_message_content = event.after.content
        author_username = event.after.author.username
        author_avatar_url = event.after.author.avatar.url
        post_date = event.after.created_at
        guild_id = event.after.channel.guild.id
        message_url = f"https://discord.com/channels/{guild_id}/{event.after.channel.id}/{event.after.id}"

        if len(old_message_content) > 800 or len(new_message_content) > 800:
            embed_description = {
                "title": "Message Edit",
                "description": f"Time At Which The Message Was Edited: {post_date}. Link To Message: {message_url}",
                "color": 65280,  # RGB value for yellow
                "thumbnail": {"url": author_avatar_url},
                "author": {"name": author_username}
            }
            embed_old_message = {
                "title": "Old Message",
                "description": old_message_content,
                "color": 65280
            }
            embed_new_message = {
                "title": "New Message",
                "description": new_message_content,
                "color": 65280
            }
            
            # Sending three separate embeds
            target_channel = self.bot.get_channel(898639531044130856)
            await target_channel.send(embed=embed_description)
            await target_channel.send(embed=embed_old_message)
            await target_channel.send(embed=embed_new_message)
        else:
            embed = {
                "title": "Message Edit",
                "description": f"Time At Which The Message Was Edited: {post_date}. Link To Message: {message_url}",
                "color": 65280,  # RGB value for yellow
                "thumbnail": {"url": author_avatar_url},
                "author": {"name": author_username},
                "fields": [
                    {"name": "Old Message", "value": old_message_content, "inline": False},
                    {"name": "New Message", "value": new_message_content, "inline": False}
                ]
            }
            
            # Sending the single embed
            target_channel = self.bot.get_channel(898639531044130856)
            await target_channel.send(embed=embed)
    
    @listen(MemberAdd)
    async def member_join_handler(self, event: MemberAdd):
        print("Member joined")

        # Convert the joined_at datetime to a Unix timestamp
        unix_timestamp = int(event.member.joined_at.timestamp())

        # Creating the embed
        embed = Embed(
            title=f"Member Joined: {event.member.display_name}",  # Setting the title dynamically
            description=f"Member Number #{event.guild.member_count}: <@{event.member.id}> joined <t:{unix_timestamp}:R> ago. \nAccount was created on: {event.member.created_at}.",
            color=0x00FF00,  # Hexadecimal code for green
            thumbnail={"url": event.member.avatar.url},  # Setting the thumbnail to the user's avatar
            footer={"text": f"User ID: {str(event.member.id)}"}
        )

        target_channel = self.bot.get_channel(898639573675032576)
        await target_channel.send(embed=embed)

    @listen(MemberRemove)
    async def member_leave_handler(self, event: MemberRemove):
        print("Member left")

        # Convert the joined_at datetime to a Unix timestamp
        unix_timestamp = int(event.member.joined_at.timestamp())

        # Grab Member Roles and construct mentions
        role_mentions = []
        for role in event.guild.roles:
            if role.id in event.member.roles:
                # Constructing the mention link for each role
                role_mention = f"<@&{role.id}>"
                role_mentions.append(role_mention)

        roles_str = ", ".join(role_mentions) if role_mentions else "No Roles"

        # Creating the embed
        embed = Embed(
            title=f"Member Left: {event.member.display_name}",  # Setting the title dynamically
            description=f"User <@{event.member.id}> joined the server <t:{unix_timestamp}:R> ago. \nAccount was created on: {event.member.created_at}.\n\n**Roles:** {roles_str}",
            color=0x00FF00,  # Hexadecimal code for green
            thumbnail={"url": event.member.avatar.url},  # Setting the thumbnail to the user's avatar
            footer={"text": f"User ID: {str(event.member.id)}"}
        )

        target_channel = self.bot.get_channel(898639573675032576)
        await target_channel.send(embed=embed)

    @listen(Component)
    async def component_interaction_handler(self, event: Component):
        # Retrieve the original context from the event
        ctx = event.ctx

        # Check if the custom_id matches the button we're interested in
        if ctx.custom_id == "rule_9":

            # Send a message in that channel
            intro_embed = Embed(
                title="Expansion Of Rule 9",
                description="The prohibition enforced by Rule 9 includes the defense (ironic or not) of the following genocides, imperialisms, bigotries, extreme right-wing ideologies, movements and states:",
                color="#36393F"
            )

            genocides_embed = Embed(
                title="Genocides",
                description="** **",
                color="#36393F"
            )
            genocides_embed.add_field(
                name="** **",
                value="The Holocaust (includes all those unjustifiably killed by Nazi, Ustaše, Horthy, Iron Guard, Bulgarian Tsarist or Mannerheim forces outside of direct combat in relation to the Second World War)\nThe Japanese Occupation of China & the Rape of Nanjing (1931-45)\nThe Armenian Genocide (1915-22)\nThe Massacres of Hutus (1996-97)\nThe Cambodian Genocide (1975-79)\nThe Rubber Terror (1885-1908)\nThe Circassian Genocide (1864-67)\nThe Rwandan Genocide (1994)\nThe Greek Genocide (1914-22)\nThe Bengal Famine (1942-43)\nThe Assyrian Genocide (1915-23)\nThe Pacification of Libya (1923-33)\nThe Irish 'Potato' Famine (1845-50)\n\nThe NATO Bombing of Yugoslavia (1999)\nThe NATO Bombing of Libya (2011)\nThe Iraq War (2003-11)",
                inline = True
            )
            genocides_embed.add_field(
                name="** **",
                value="The Anfal Campaign (1986-89)\nThe Palestinian Genocide & an-Nakbah (1948-present)\nThe Bangladesh Genocide (1971)\nThe Donbas War (2014-22)\nOperation Condor (1968-89)\nThe Rhodesian Bush War (1964-79)\nThe Transatlantic Slave-Trade & American Slavery (1526-1865)\nThe Colonisation of Sápmi (1607-present)\nThe Colonisation of the Americas (1492-present)\nThe Japanese Occupation of Korea (1910-45)\nThe Colonisation of Hawai'i (1900-present)\nThe Saudi-led Intervention in Yemen (2014-present)\nThe Bosnian Genocide (1992-95)\nSegregation in the United States (1865-1964)\nThe Darfur Genocide (2003-present)\nThe Yazidi Genocide (2014-15)\nThe Indonesian Genocide (1965-66)",
                inline = True
            )
            
            imperialism_embed = Embed(
                title="Imperialism",
                description="** **",
                color="#36393F"
            )
            imperialism_embed.add_field(
                name="** **",
                value="American Imperialism\nJapanese Imperialism\nRussian Imperialism\nBritish Imperialism\nFrench Imperialism\nSpanish Imperialism\nPortuguese Imperialism\nItalian Imperialism\nOttoman Imperialism\nChinese Imperialism\nAustrian Imperialism\nSwedish Imperialism\nDanish Imperialism\nDutch Imperialism\nBelgian Imperialism",
                inline=True
            )
            imperialism_embed.add_field(
                name="** **",
                value="Canadian Imperialism\nGerman Imperialism\nSoviet Imperialism\nYugoslav Imperialism\nNorwegian Imperialism\nBrazilian Imperialism\nIranian Imperialism\nAustralian Imperialism\nNew Zealandic Imperialism\nSaudi Imperialism\nQatari Imperialism\nBahraini Imperialism\nEmirati Imperialism\nIsraeli Imperialism",
                inline=True
            )

            ideologies_embed = Embed(
                title="Ideologies",
                description="** **",
                color="#36393F"
            )
            ideologies_embed.add_field(
                name="** **",
                value="Fascism (Third Position/Third Way)\nNazism (National-Socialism/Hitlerism)\nItalian Fascism (Mussolinism)\nSpanish Fascism (Falangism/Francoism)\nNational Syndicalism\nDuginism (Fourth Way/National-Bolshevism)",
                inline=True
            )
            ideologies_embed.add_field(
                name="** **",
                value="Chilean Fascism (Pinochetism)\nSocial-Darwinism (Nordicism/Han Nationalism/Aryanism)\nHindutva\nMosleyism\nUltra-nationalism\nIrredentism\nConservatism\nLegionarism\nMonarchism\nStrasserism",
                inline=True
            )

            bigotries_embed = Embed(
                title="Bigotries",
                description="** **",
                color="#36393F"
            )
            bigotries_embed.add_field(
                name="** **",
                value="Anti-Semitism\nAntiziganism\nHomophobia\nTransphobia\nBiphobia\nMisogyny\nQueerphobia\nAbleism",
                inline=True
            )
            bigotries_embed.add_field(
                name="** **",
                value="Pol-Potism\nEugenicism\nWhite Supremacism (White Identitarianism/Race Realism/Racialism/Racism)",
                inline=True
            )

            states_embed = Embed(
                title="States",
                description="** **",
                color="#36393F"
            )
            states_embed.add_field(
                name="** **",
                value="The German Reich (1933-45)\nThe Kingdom of Italy (1922-43)\nThe Italian Social Republic (1943-45)\nThe Kingdom of Hungary (1920-46)\nThe Empire of Japan (1868-1947)\nThe Slovak Republic (1939-45)\nThe Tsardom of Bulgaria (1941-46)\nThe Kingdom of Thailand (1941-45)\nThe Russian Empire (1904-17)\nThe German Empire (1881-1918)\nThe Republic of Cuba (1952-1959)\nThe Republic of Chile (1974-90)\nThe Kingdom of Romania (1941-44)\nThe French State (1940-44)\nThe United States of America (1776-present)\nThe Confederate States of America (1861-1865)\nThe Republic of Korea (1948-60, 1963-87)\nThe Kingdom of England (1607-1707)",
                inline=True
            )
            states_embed.add_field(
                name="** **",
                value="The Republic of Vietnam (1955-75)\nThe United Kingdom of Great Britain and Northern Ireland (1707-present)\nDemocratic Kampuchea (1975-79)\nThe State of Israel (1948-present)\nCanada (1982-present)\nThe Russian Federation (1991-present)\nThe United Arab Emirates (1971-present)\nThe Kingdom of Saudi Arabia (1932-present)\nThe State of Qatar (1971-present)\nThe Kingdom of Bahrain (1971-present)\nThe Kingdom/Republic of France (1524-present)\nThe Kingdom/Republic/State of Spain (1492-present)\nThe Kingdom/Republic of Portugal (1415-1975)\nThe Islamic State (of Iraq and the Levant/Syria) (1999-2019)",
                inline=True
            )

            await ctx.send(embeds=[intro_embed, genocides_embed, imperialism_embed, ideologies_embed, bigotries_embed, states_embed], ephemeral=True)

# Vetting Question Embeds -> LEARNING
learning_question_2 = Embed(
    title="[2 / 9] What Are Your Views On Capitalism, And Why?",
    description="We do not require that you are a socialist/communist to join this server, for common myths or misunderstandings of socialism, please visit: <#1005887212614852618>.",
    color="#2986cc"
)
learning_question_3 = Embed(
    title="[3 / 9] What Would You Characterise Your Ideology As?",
    description="Include any thinkers or figures that have influenced your ideological views and what you have taken from them, mentioning key works that you have read may be helpful.",
    color="#2986cc"
)
learning_question_4 = Embed(
    title="[4 / 9] What Are Your Views On Lenin, Stalin and Mao? ",
    description="We do not require that you take a specific line or position on any of the figures mentioned, for common myths, misunderstandings, or discussion topics, please visit: <#1005887293065801768>.",
    color="#2986cc"
)
learning_question_5 = Embed(
    title="[5 / 9] What Are Your Views On AES States?",
    description="AES (actual existing socialism) states covers examples such as China, Cuba, the DPRK, the USSR. If you do not view them as socialist, please explain why.",
    color="#2986cc"
)
learning_question_6 = Embed(
    title="[6 / 9] What Are Your Views On National Liberation Movements?",
    description="This includes movements within existing nations, such as Black Liberation, Indigenous Land Back Movements, Palestine, Kurdistan, and Kosovo. if you do not support liberation movements, please explain why.",
    color="#2986cc"
)
learning_question_7 = Embed(
    title="[7 / 9] Do You Support LGBTQIA+ People And Movements For Their Liberation?",
    description="This includes specifically transgender people, intersex people, gay/lesbian people. if you are not supportive of these people / identities or movements, please explain why.",
    color="#2986cc"
)
learning_question_8 = Embed(
    title="[8 / 9] Do You Believe Communists Should Support Multipolarity?",
    description="Multipolarity takes the form of strengthening capitalist anti-US/West nations such as Russia, Iran, Belarus. Please explain why or why not. ",
    color="#2986cc"
)
learning_question_9 = Embed(
    title="[9 / 9] Did You Read The <#1005886992166420580>?",
    description="It is not required that you read the thread clarifications expanding on the rules. if you have read them, do you agree to follow them?",
    color="#2986cc"
)

# Vetting Question Embeds -> EDUCATED
educated_question_2 = Embed(
    title="[2 / 13] What Are Your Views On National Liberation Movements?",
    description="This includes movements within existing nations, such as Black Liberation, Indigenous Land Back Movements, Palestine, Kurdistan, and Kosovo. if you do not support liberation movements, please explain why.",
    color="#2986cc"
)
educated_question_3 = Embed(
    title="[3 / 13] Do You Support LGBTQIA+ People And Movements For Their Liberation?",
    description="This includes specifically transgender people, intersex people, gay/lesbian people. if you are not supportive of these people / identities or movements, please explain why.",
    color="#2986cc"
)
educated_question_4 = Embed(
    title="[4 / 13] Do You Believe Communists Should Support Multipolarity?",
    description="Multipolarity takes the form of strengthening capitalist anti-US/West nations such as Russia, Iran, Belarus. Please explain why or why not. ",
    color="#2986cc"
)
educated_question_5 = Embed(
    title="[5 / 13] Did You Read The <#1005886992166420580>?",
    description="It is not required that you read the thread clarifications expanding on the rules. if you have read them, do you agree to follow them?",
    color="#2986cc"
)
educated_question_6 = Embed(
    title="[6 / 13] What Ideology Would You Say You Mostly Align With?",
    description="Include Any Thinkers Or Figures That Have Influenced Your Ideological Views And What You Have Taken From Them, Mentioning Key Works That You Have Read May Be Helpful.",
    color="#2986cc"
)
educated_question_7 = Embed(
    title="[7 / 13] What Social Relations Must Be Produced To Constitute A Capitalist Mode Of Production?",
    description="**[Key Words]:** Mode of Production; Production for Exchange; Wage Labor; Private Property; Bourgeoisie and Proletariat (Class); Capital; Valorization; Accumulation",
    color="#2986cc"
)
educated_question_8 = Embed(
    title="[8 / 13] What Are The Characteristics Of The Communist Mode Of Production, In Both The Lower Phase (AKA: Socialism) And The Higher Phase (AKA: Communism)?",
    description="**[Key Words]:** Transitional; Mode of Production; Higher and Lower Phase; Money; State; Commodity; Labor",
    color="#2986cc"
)
educated_question_9 = Embed(
    title="[9 / 13] Explain The Methodology Of Marx, Showing How Marx Reconciles The Inconsistencies Within Materialism And Idealism Via Dialectics.",
    description="**[Key Words]:** Contradiction; Materialism; Dialect; Transhistoricism; Hegel/Aristotle/Mao/Engels; Holistic; Dynamic; Social Relations; Dialectical Idealism; Production and Reproduction; Law of Dialect;",
    color="#2986cc"
)
educated_question_10 = Embed(
    title="[10 / 13] What Differentiates Scientific Socialism From Utopian Socialism? Please Give An Example Of Both.",
    description="**[Key Words]:** Moral/Normative Arguments; Class Character; Dialectical Materialism; Interchangeable with Communism; Robert Owen; Anarchism",
    color="#2986cc"
)
educated_question_11 = Embed(
    title="[11 / 13] Explain At Least Three Theoretically Derived Innovations Lenin Made To Marxism.",
    description="**[Key Words]:** Imperialism; Vanguard; Democratic Centralism; War Communism; Revolutionary Defeatism; Particulars of Legal and Illegal Struggle; Dual Power; Theory of Socialist Industrialization",
    color="#2986cc"
)
educated_question_12 = Embed(
    title="[12 / 13] What Is The Materialist Conception Of The History Of The State In Terms Of Its: Genesis, Development, Withering Away",
    description="**[Key Words]:** Dictatorship of the Proletariat/Bourgeoisie/Ruling Class; Withering; Capturing the State; Smashing Bourgeois State; Class Conflict; Social Relations; Means of Production; Distinct Interests",
    color="#2986cc"
)
educated_question_13 = Embed(
    title="[13 / 13] How Should The Working Class Organize To Take Class Power?",
    description="[Key Words]: Party; Oppressed Groups; Democratic Centralism; Tactics; Go to the Masses; Praxis",
    color="#2986cc"
)