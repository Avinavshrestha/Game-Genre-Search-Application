from django.core.management.base import BaseCommand
from games.models import GameGenre  # Replace 'yourapp' with your app name

class Command(BaseCommand):
    help = 'Populate the GameGenre database with sample data'

    def handle(self, *args, **kwargs):
        genres = [
            {
                "title": "First-person Shooter",
                "description": "First-person shooters (FPS) are immersive action games that focus on gun-based combat from a first-person perspective. Players engage in fast-paced gameplay, utilizing quick reflexes, precise aiming, and strategic thinking to navigate through 3D environments. These games often feature a blend of single-player campaigns and competitive multiplayer modes, where players can complete objectives, explore expansive worlds, and engage in intense shootouts. Notable examples include classics and modern titles such as 'Wolfenstein 3D', 'Doom', 'GoldenEye 007', and contemporary hits like 'Call of Duty: Warzone'.",
                "games": "Wolfenstein 3D, Doom, GoldenEye 007, Half-Life, Halo: Combat Evolved, Call of Duty 4: Modern Warfare, Overwatch"
            },
            {
                "title": "Role-Playing Game",
                "description": "Role-playing games (RPGs) allow players to immerse themselves in richly crafted fictional worlds, assuming the roles of unique characters. Players embark on epic quests, engage in battles, and make meaningful choices that shape their character’s development and the overarching narrative. RPGs often feature deep lore, intricate storylines, and character customization options that enable skill and ability enhancement throughout the game. This genre encompasses various gameplay styles, ranging from traditional turn-based systems to real-time action mechanics. Renowned RPGs include 'Final Fantasy VII', 'The Elder Scrolls V: Skyrim', and 'The Witcher 3: Wild Hunt'.",
                "games": "Final Fantasy VII, The Elder Scrolls V: Skyrim, The Witcher 3: Wild Hunt, Dark Souls, Persona 5, Mass Effect 2"
            },
            {
                "title": "Action-Adventure",
                "description": "Action-adventure games seamlessly blend action elements with adventure, emphasizing exploration, puzzle-solving, and combat mechanics. Players control characters navigating diverse environments, battling enemies, and completing missions. This genre often incorporates rich storytelling and character progression, inviting players to uncover mysteries and develop their skills as they advance. The dynamic gameplay experience is filled with challenges and surprises, making action-adventure games incredibly engaging. Notable titles include 'The Legend of Zelda: Breath of the Wild', 'Uncharted 4: A Thief's End', and 'God of War'.",
                "games": "The Legend of Zelda: Breath of the Wild, Uncharted 4: A Thief's End, God of War, Tomb Raider, Assassin's Creed Odyssey"
            },
            {
                "title": "Platformer",
                "description": "Platformer games challenge players to guide characters through levels filled with platforms, obstacles, and enemies. Gameplay often involves jumping, running, and climbing, with players collecting items and power-ups to enhance their abilities. The genre ranges from 2D side-scrollers to fully 3D experiences, each offering unique mechanics and challenges. Emphasizing precise timing and quick reflexes, platformers provide accessible yet challenging gameplay for all skill levels. Iconic platformers include 'Super Mario Bros.', 'Sonic the Hedgehog', and 'Celeste'.",
                "games": "Super Mario Bros., Sonic the Hedgehog, Celeste, Hollow Knight, Ori and the Blind Forest"
            },
            {
                "title": "Simulation",
                "description": "Simulation games aim to replicate real-world activities and scenarios, allowing players to engage in experiences that mirror life or specific professions. This genre ranges from life simulation, where players manage daily activities, to complex systems like city-building or flight simulators. Simulation games provide tools for players to create, manage, and make decisions, fostering agency and realism. The diversity of this genre caters to a wide range of interests, appealing to players who enjoy strategic planning and management. Popular titles include 'The Sims', 'SimCity', and 'Microsoft Flight Simulator'.",
                "games": "The Sims series, SimCity, Microsoft Flight Simulator, Farming Simulator, Cities: Skylines"
            },
            {
                "title": "Puzzle",
                "description": "Puzzle games challenge players to apply logic, strategy, and critical thinking to solve problems and complete challenges. This genre encompasses a wide range of gameplay styles, from matching colors or shapes to complex brain teasers requiring careful planning. Puzzle games can be casual and accessible or deeply challenging, providing a satisfying mental workout. Many modern puzzle games incorporate unique mechanics that encourage players to think creatively and adapt their strategies as they progress. Classic examples include 'Tetris', 'Portal', and 'Candy Crush Saga'.",
                "games": "Tetris, Portal, The Witness, Candy Crush Saga, Monument Valley"
            },
            {
                "title": "Fighting",
                "description": "Fighting games emphasize direct combat between characters in one-on-one or team-based matches. Players utilize a variety of moves, combos, and strategies to defeat opponents, featuring a roster of unique characters with distinct abilities and fighting styles. Known for competitive gameplay, fighting games have a thriving community with tournaments showcasing skilled players. This genre ranges from traditional 2D fighters to 3D brawlers, each offering unique mechanics and experiences. Notable fighting games include 'Street Fighter II', 'Mortal Kombat', and 'Super Smash Bros.'.",
                "games": "Street Fighter II, Mortal Kombat, Super Smash Bros., Tekken 7, Dragon Ball FighterZ"
            },
            {
                "title": "Racing",
                "description": "Racing games simulate the experience of driving various vehicles on tracks or open environments. Players compete against each other or against the clock, navigating courses at high speeds while avoiding obstacles and managing vehicle performance. The genre includes arcade racing emphasizing fun and accessibility and realistic simulations replicating real-world physics. Racing games often feature extensive vehicle customization and various modes, including time trials, championships, and online multiplayer. Popular racing games include 'Mario Kart 8 Deluxe', 'Gran Turismo Sport', and 'Need for Speed: Heat'.",
                "games": "Mario Kart 8 Deluxe, Gran Turismo Sport, Forza Horizon 4, Need for Speed: Heat, F1 2021"
            },
            {
                "title": "Stealth",
                "description": "Stealth games challenge players to navigate environments without detection by enemies. Strategic thinking, timing, and cunning are essential as players achieve objectives while avoiding confrontation. Gameplay focuses on careful planning, observation, and utilizing tools or gadgets to manipulate surroundings. Rich narratives and immersive worlds encourage exploration and experimentation. This genre appeals to players who enjoy strategic gameplay and the thrill of outsmarting opponents. Noteworthy titles include 'Metal Gear Solid', 'Splinter Cell', and 'Assassin's Creed'.",
                "games": "Metal Gear Solid, Splinter Cell, Hitman, Assassin's Creed, Dishonored"
            },
            {
                "title": "Horror",
                "description": "Horror games evoke fear, tension, and suspense through unsettling narratives, eerie atmospheres, and terrifying enemies. Players must survive against overwhelming odds, uncovering dark secrets or escaping monstrous threats. The genre employs psychological and visceral elements to create a sense of dread, immersing players in experiences that can be exhilarating and terrifying. Horror games often incorporate mechanics such as limited resources and puzzle-solving to heighten the tension. Iconic horror titles include 'Resident Evil', 'Silent Hill', and 'Amnesia: The Dark Descent'.",
                "games": "Resident Evil series, Silent Hill 2, Amnesia: The Dark Descent, Outlast, Dead Space"
            },
            {
                "title": "Survival",
                "description": "Survival games immerse players in harsh environments where they must gather resources, craft items, and fend off threats to stay alive. Players face challenges like hunger, environmental dangers, and hostile creatures, requiring strategic thinking and adaptability. The genre emphasizes exploration, resource management, and crafting, encouraging players to build shelters and develop survival skills. Survival games can range from realistic simulations to fantastical adventures, providing varied experiences that test ingenuity. Notable survival titles include 'Minecraft', 'ARK: Survival Evolved', and 'Don't Starve'.",
                "games": "Minecraft, ARK: Survival Evolved, Don't Starve, The Forest, Rust"
            },
            {
                "title": "Open World",
                "description": "Open-world games offer expansive environments for players to explore freely. These games create a sense of immersion and agency, allowing players to engage in various activities, complete quests, or roam at their own pace. The genre often features dynamic narratives, rich lore, and diverse ecosystems, contributing to an engaging gameplay experience. Players can interact with NPCs, embark on side missions, and uncover hidden secrets, making open-world games highly replayable. Renowned titles include 'Grand Theft Auto V', 'Red Dead Redemption 2', and 'Cyberpunk 2077'.",
                "games": "Grand Theft Auto V, Red Dead Redemption 2, The Legend of Zelda: Breath of the Wild, Far Cry 5, Cyberpunk 2077"
            },
            {
                "title": "Multiplayer Online Battle Arena (MOBA)",
                "description": "MOBA games feature two teams competing in strategic combat, typically with unique characters possessing distinct abilities. Players collaborate to defeat the opposing team by destroying their base while navigating a map filled with obstacles and resources. The genre emphasizes teamwork, strategy, and quick decision-making, with each match offering a unique experience based on player choices. MOBAs often include leveling systems, allowing characters to gain strength during matches. Popular titles in this genre include 'League of Legends', 'Dota 2', and 'Smite'.",
                "games": "League of Legends, Dota 2, Smite, Heroes of the Storm, Arena of Valor"
            },
            {
                "title": "Massively Multiplayer Online (MMO)",
                "description": "MMO games allow thousands of players to interact in persistent virtual worlds, offering a blend of role-playing, combat, and social experiences. Players create characters, complete quests, and engage in player-driven economies while collaborating or competing with others. This genre emphasizes community and exploration, providing diverse gameplay experiences through dynamic events and expansive content updates. MMOs often include character progression and customization, creating a sense of accomplishment. Notable MMOs include 'World of Warcraft', 'Final Fantasy XIV', and 'Guild Wars 2'.",
                "games": "World of Warcraft, Final Fantasy XIV, Guild Wars 2, Elder Scrolls Online, Black Desert Online"
            },
            {
                "title": "Card Game",
                "description": "Card games are strategic games where players build decks and engage in battles using cards representing characters, spells, or items. This genre emphasizes strategy, resource management, and tactical decision-making, requiring players to think critically and adapt to opponents' moves. Digital card games often feature unique mechanics and themes, attracting diverse audiences. Popular titles include 'Hearthstone', 'Magic: The Gathering Arena', and 'Gwent: The Witcher Card Game'.",
                "games": "Hearthstone, Magic: The Gathering Arena, Gwent: The Witcher Card Game, Legends of Runeterra, Yu-Gi-Oh! Duel Links"
            },
            {
                "title": "Text-Based Adventure",
                "description": "Text-based adventure games immerse players in narrative-driven experiences, where they explore worlds and solve puzzles primarily through written descriptions. This genre relies on player choices and imagination, inviting them to engage with characters and environments through text commands. While often considered retro, modern iterations continue to captivate audiences with rich storytelling and interactive narratives. Notable titles include 'Zork', '80 Days', and 'Choice of Robots'.",
                "games": "Zork, 80 Days, Choice of Robots, Sorcery!, Emily is Away"
            }
        ]

        for genre_data in genres:
            genre, created = GameGenre.objects.get_or_create(
                title=genre_data["title"],
                defaults={
                    "description": genre_data["description"],
                    "games": genre_data["games"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created genre: {genre.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Genre already exists: {genre.title}'))
