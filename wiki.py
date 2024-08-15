from interactions import Extension, Embed
from interactions.ext.hybrid_commands import hybrid_slash_command, HybridContext

class WikiCommands(Extension):
    def __init__(self, bot):
        self.bot = bot

    @hybrid_slash_command(name="wikilist", description="Display Information About The UMP Wiki", scopes=[898568341499838514])
    async def wikilist_function(self, ctx: HybridContext):
        embed = Embed(
            title="What is the United Marxist Pact Wiki?",
            description="The UMP Wiki aims to provide a comprehensive collection of miniature factbooks & links to key works on a plethora of Authors across the centuries of Marxist History. \n\nSimilarly, we are expanding the collection constantly, and aim to include information on tackling common socialist myths, information on socialist movements, and AES nations, as well as analysis of key works and terminology used in Marxism.",
            color="#000000"
        )
        embed.set_author(name="United Marxist Pact", icon_url=ctx.guild.icon.url)

        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="marx", description="Display Information About Karl Marx", scopes=[898568341499838514])
    async def marx_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Karl Marx",
            description="**Karl Marx (1818 - 1883)** was a German philosopher, economist, and political theorist known for his revolutionary ideas.\n\n"
                        "He shortly wrote for a liberal Cologne newspaper called Rheinische Zeitung, before it was banned from publication and Marx left Prussia "
                        "moving to Paris, where he met Friedrich Engels. Marx is best known as the author of the seminal works including “The Communist Manifesto” and “Capital: a Critique of Political Economy” "
                        "which have influenced generations of political leaders and socio-economic thinkers.\n\n"
                        "** **",
            color="#FF0000"
        )
        embed.set_author("1800s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Karl_Marx_001.jpg/330px-Karl_Marx_001.jpg")
        embed.add_field(name="Areas of Work", value="Critique of Political Economy\nPhilosophy\nScientific Socialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="engels", description="Display Information About Friedrich Engels", scopes=[898568341499838514])
    async def engels_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Friedrich Engels",
            description="**Friedrich Engels (1820 - 1895)** was a German socialist philosopher and the closest collaborator and confident of Karl Marx in the foundation of Communism.\n\n "
                        "Born into a wealthy family, he was radicalized by the harsh conditions he observed among the working class in industrial cities "
                        "his experiences in Manchester, England, where he worked at his family’s mill, turned him towards socialism.\n\n " 
                        " Engels co-authored “The Communist Manifesto” with Karl Marx and made significant contributions to the ideas of historical materialism, philosophy, economics, and other fields that laid the foundations for socialist change.\n"
                        "** **",
            color="#FF0000"
        )
        embed.set_author("1800s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/2/21/Friedrich_Engels_portrait_%28cropped%29.jpg")
        embed.add_field(name="Areas of Work", value="Critique of Political Economy\nPhilosophy\nScientific Socialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="lenin", description="Display Information About Vladimir Ilyich Ulyanov", scopes=[898568341499838514])
    async def lenin_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Vladimir Ilyich Ulyanov",
            description="**Vladimir Ilyich Ulyanov (1870 - 1924)** was a Russian revolutionary, political theorist, and politician. Born in Simbirsk, Russia, to an upper-middle-class family, Lenin was radicalized at a young age following the execution of his brother for plotting the assassination of the Tsar.\n\n "
                        "Lenin became a key figure in the Russian Social-Democratic Labour Party and led its Bolshevik wing and became known leading the October Revolution in 1917.\n\n "
                        "Lenin’s works, such as “Imperialism, the Highest Stage of Capitalism” and “State and Revolution”, broadly cover topics including the critique of capitalism, the theory of imperialism, the role of the state in society, the necessity of proletarian revolution, and the theoretic inadequacies of social democracy in achieving revolution to establish the dictatorship of the proletariat.\n"
                        "** **",
            color="#FF0000"
        )
        embed.set_author("1900s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/c/c0/Lenin_in_1920_%28cropped%29.jpg")
        embed.add_field(name="Areas of Work", value="Organisation\nRevolution\nImperialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="stalin", description="Display Information About Joseph Vissarionovich Stalin", scopes=[898568341499838514])
    async def stalin_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Joseph Vissarionovich Stalin",
            description="**Joseph Vissarionovich Stalin (1878 - 1953)** was a pivotal figure in the socialist movement, rising from humble origins in Gori, Georgia, to become a prominent leader within the Bolshevik ranks. Known for his strategic prowess and dedication to Marxist-Leninist principles, Stalin played a crucial role in the October Revolution of 1917, which established Soviet rule.\n\n "
                        "Stalin's contributions to socialist thought are encapsulated in works such as 'Foundations of Leninism' and 'Dialectical and Historical Materialism' In these writings, he expounded upon Marxist theory, particularly emphasizing the role of class struggle and the necessity of a vanguard party in achieving socialist revolution.\n"
                        "** **",
            color="#FF0000"
        )
        embed.set_author("1900s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/StalinCropped1943%28b%29.jpg/220px-StalinCropped1943%28b%29.jpg")
        embed.add_field(name="Areas of Work", value="Leninism\nDialectical Materialism\nScientific Socialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="connolly", description="Display Information About James Connolly", scopes=[898568341499838514])
    async def connolly_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="James Connolly",
            description="**James Connolly (1868 - 1916)** was born in Edinburgh, Scotland to Irish parents. He is said to have first come to Ireland in his youth as a member of the British Army " 
                        " and became active in The Socialist movement in Edinburgh in the early 1890s. In 1896, he moved to Ireland and founded the Irish Socialist Republican Party "
                        " providing lectures on socialism in Britain and U.S. \n\n"
                        " In 1902 he emigrated to U.S. and became a member of the Socialist Labour Party (U.S.) and the Industrial Workers of the World "
                        " He was also the Commandant General of Dublin Division of the Army of the Republic, before being executed following the 1916 Uprising.",
            color="#FF0000"
        )
        embed.set_author("1800s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/2/2d/James_Connolly2.jpg")
        embed.add_field(name="Areas of Work", value="Syndicalism\nNational Liberation\nSocialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="gonzalo", description="Display Information About Abimael Guzmán (known as Chairman Gonzalo)", scopes=[898568341499838514])
    async def gonzalo_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Abimael Guzmán",
            description="**Abimael Guzmán (1934 - 2021)** a Peruvian revolutionary, was primarily known for his role as the founder and leader of the Shining Path, "
                        "a Maoist guerrilla insurgent group. His socialist work focused on advocating for the overthrow of the Peruvian government and establishing a communist "
                        "state based on Maoist principles.\n\n Guzmán's ideology emphasized the need for armed struggle to achieve socialist revolution, targeting perceived class enemies "
                        "and engaging in violent tactics to advance his cause. ",
            color="#FF0000"
        )
        embed.set_author("1900s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Gonzalo_Enhanced_Large.png/1200px-Gonzalo_Enhanced_Large.png")
        embed.add_field(name="Areas of Work", value="Militancy\nMaoism\nAnti-Revisionism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="deleon", description="Display Information About Daniel De Leon", scopes=[898568341499838514])
    async def deleon_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Daniel De Leon",
            description="Daniel De Leon (1852 – 1914) was born in Curaçao but moved to the United States during some time in 1872-1874 while studying medicine and several languages. "
                        "After serving as a school teacher, and then as an attorney he finally became a lecturer at Columbia University before embracing a more radically socialist "
                        "path.\n\nDe Leon is a co-founder with both the Industrial Worker of the World, as well as the Socialist Labor Party. "
                        "He is often regarded as the father of socialist revolutionary industrial unionism. His ideas and philosophy contributed to the creations of Socialist "
                        "Labor parties across the world, including: Australia, the United Kingdom, Canada, and the Socialist Trade and Labor Alliance.\n\n"
                        "George Seldes quotes Lenin saying on the fifth anniversary of the revolution, '... What we have done in Russia is accept the De Leon "
                        "interpretation of Marxism, that is what the Bolsheviki adopted in 1917.'",
            color="#FF0000"
        )
        embed.set_author("1800s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/c/cb/Daniel-DeLeon-1902.jpg")
        embed.add_field(name="Areas of Work", value="Socialism\nIndustrial Union\nMarxism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="hoxha", description="Display Information About Enver Hoxha", scopes=[898568341499838514])
    async def hoxha_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Enver Hoxha",
            description="**Enver Hoxha (1908 - 1985)** was an Albanian communist leader known for his role in establishing and leading the socialist state of Albania. "
                        " He served as the First Secretary of the Party of Labour of Albania from 1941 until his death in 1985. Hoxha pursued a strict Marxist-Leninist ideology, "
                        "focused on industrialization, collectivization of agriculture, and the suppression of perceived internal and external threats to socialism.\n\n"
                        "He also actively supported various communist and socialist movements worldwide, providing material and ideological assistance to revolutionary groups in other countries. Hoxha's dedication to socialist organization both at home and abroad solidified his reputation as a stalwart defender of Marxist-Leninist principles. ",
            color="#FF0000"
        )
        embed.set_author("1900s | Authors")
        embed.set_thumbnail(url="https://alphahistory.com/coldwar/wp-content/uploads/2016/05/enverhoxha.jpg")
        embed.add_field(name="Areas of Work", value="Class Struggle\nSelf-Reliance\nAnti-Revisionism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="mao", description="Display Information About Mao Zedong", scopes=[898568341499838514])
    async def mao_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Mao Zedong",
            description="**Mao Zedong (1893 - 1976)** was a Chinese revolutionary, political theorist, and politician. Hailing from Shaoshan, China, Mao used his experiences with China's peasants and workers, a dedication to Marxist ideals and led the Communist Party of China during the revolution of 1949.\n\n "
                        "Mao's unique approach to socialism prioritized agrarian reform, industrialization, and empowering the peasantry, overseeeing ambitious experiments like the Great Leap Forward and the Cultural Revolution.\n\n "
                        "Central to Mao's philosophy were his writings, notably 'On Contradiction' and 'On Practice.' These works elucidate Marxist theory, emphasizing dialectical materialism and the significance of revolutionary action. Mao's ideas formed the bedrock of his vision for transforming China through continuous revolution and mass mobilization.\n"
        "** **",
            color="#FF0000"
        )
        embed.set_author("1900s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/0/0a/Mao_Zedong_in_1959_%28cropped%29.jpg")
        embed.add_field(name="Areas of Work", value="Class Struggle\nSelf-Reliance\nDialectical Materialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="kautsky", description="Display Information About Karl Kautsky", scopes=[898568341499838514])
    async def kautsky_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Karl Kautsky",
            description="**Karl Kautsky (1854 - 1938)** was a prominent Czech-German Marxist theoretician and a key figure in the Social Democratic Party of Germany (SPD). Born in Prague, he studied history and philosophy before becoming involved in socialist politics. Kautsky was an influential editor of the SPD's theoretical journal, 'Die Neue Zeit,' and a close associate of Friedrich Engels. \n\nHe is best known for his works on Marxist theory and his role in the Second International, where he argued for a democratic and evolutionary approach to socialism, in contrast to the revolutionary methods later adopted by Lenin and the Bolsheviks. \n\nKautsky's extensive writings helped shape the ideological foundation of social democracy in the early 20th century.",
            color="#FF0000"
        )
        embed.set_author("1800s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Karl_Kautsky_01.jpg/220px-Karl_Kautsky_01.jpg")
        embed.add_field(name="Areas of Work", value="Class Struggle\nSelf-Reliance\nDialectical Materialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="rosa", description="Display Information About Rosa Luxemburg", scopes=[898568341499838514])
    async def rosa_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Rosa Luxemburg",
            description="**Rosa Luxemburg (1871 - 1919)** was a Polish-German Marxist theorist, philosopher, and revolutionary socialist. Born in Zamość, Poland, she became politically active at a young age and later moved to Germany, where she joined the Social Democratic Party (SPD). \n\nLuxemburg was a fierce critic of the SPD's reformist tendencies and co-founded the more radical Spartacus League, which later became the Communist Party of Germany (KPD). Her notable works include 'The Accumulation of Capital' and 'The Mass Strike,' where she argued for spontaneous mass action and workers' democracy. \n\nLuxemburg's commitment to revolutionary socialism and her opposition to World War I ultimately led to her arrest and assassination during the failed Spartacist uprising in 1919.",
            color="#FF0000"
        )
        embed.set_author("1800s | Authors")
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Rosa_Luxemburg.jpg/220px-Rosa_Luxemburg.jpg")
        embed.add_field(name="Areas of Work", value="Class Struggle\nSelf-Reliance\nDialectical Materialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="che", description="Display Information About Che Guevara", scopes=[898568341499838514])
    async def che_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="Che Guevara",
            description="**Che Guevara (1928 - 1967)**, born Ernesto Guevara in Rosario, Argentina, was a revolutionary leader, physician, and guerrilla warfare strategist. Guevara played a pivotal role in the Cuban Revolution alongside Fidel Castro, helping to overthrow the Batista regime in 1959. \n\nAfter the revolution, he held various key governmental positions in Cuba and authored influential works on guerrilla warfare and Marxist theory. Guevara's vision of global revolution led him to support insurgencies in the Congo and later in Bolivia, where he was captured and executed by Bolivian forces in 1967. \n\nHis legacy as a symbol of anti-imperialist struggle and socialist ideals endures, making him an iconic figure in revolutionary movements worldwide.",
            color="#FF0000"
        )
        embed.set_author("1900s | Authors")
        embed.set_thumbnail(url="https://cdn.britannica.com/44/11344-050-9456729E/Che-Guevara.jpg")
        embed.add_field(name="Areas of Work", value="Class Struggle\nSelf-Reliance\nDialectical Materialism", inline=False)
        
        await ctx.send(embeds=[embed])

    @hybrid_slash_command(name="willich", description="Display Information About August Willich", scopes=[898568341499838514])
    async def willich_wiki_function(self, ctx: HybridContext):
        embed = Embed(
            title="August Willich",
            description="**August Willich (1810 – 1878)**, was Prussian military officer and noble that gave up both his rank and noble title to become a communist revolutionary during the Revolutions of 1848. After that revolution failed he would move to the United States specifically to join the Union Army and fight against slavery and was instrumental in bringing German socialist revolutionaries into the conflict."
                        "\n\nWillich famously wanted to duel Karl Marx for what he viewed as unacceptable conservatism on the part of Marx. He was also aide-de-camp to Friedrich Engles."
                        "\n\nWhile in the United States, he would be a foundational member of a Hegalian think-tank known as the Ohio Hegelians as well as take a prominent role in the Civil War earning the rank of Brigadier General of the Union Army and is credited for his role in the Chattanooga Campaign where his capture of a vital location is credited with opening the door to Sherman's march on Atlanta, a pivotal moment in the success of the Union in the civil war."
                        "\n\nMarx himself would later eulogize Willich as a true revolutionary: 'In the Civil War in North America, Willich showed that he is more than a visionary'",
            color="#FF0000"
        )
        embed.set_author("1800s | Revolutionaries")
        embed.set_thumbnail(url="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ9m_wzS-5p9nKUUBA_QBz2USunZs0OgOHosmnmdAQ8V07s6AfD")
        embed.add_field(name="Areas of Work", value="Communism\nRevolution\nAbolition", inline=False)
        
        await ctx.send(embeds=[embed])