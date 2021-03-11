import random

MatureWhiteCards = ["Flying sex snakes.", "Michelle Obama's arms.", "German dungeon porn.", "White people.",
               "Getting so angry that you pop a boner.", "Tasteful sideboob.", "Praying the gay away.",
               "Two midgets shitting into a bucket.", "MechaHitler.", "Being a motherfucking sorcerer.",
               "A disappointing birthday party.", "Puppies!", "A windmill full of corpses.", "Guys who don't call.",
               "Racially-biased SAT questions.", "Dying.", "Steven Hawking talking dirty.", "Being on fire.",
               "A lifetime of sadness.", "An erection that lasts longer than four hours.", "AIDS",
               "Same-sex ice dancing.", "Glenn Beck catching his scrotum on a curtain hook.", "The Rapture.",
               "Pterodactyl eggs.", "Crippling debt.", "Eugenics.", "Exchanging pleasantries.", "Dying of dysentery.",
               "Roofies.", "Getting naked and watching Nickelodeon.", "The forbidden fruit.", "Republicans.",
               "The Big Bang.", "Anal beads.", "Amputees.", "Men.", "Surprise sex!", "Kim Jong-il.",
               "Concealing a boner", "Agriculture.", "Glenn Beck being harried by a swarm of buzzards.",
               "Making a pouty face.", "A salty surprise.", "The Jews.", "Charisma.",
               "YOU MUST CONSTRUCT ADDITIONAL PYLONS.", "Panda sex.", "Taking off your shirt.", "A drive-by shooting.",
               "Ronald Reagan.", "Morgan Freeman's voice.", "Breaking out into song and dance.", "Jewish fraternities.",
               "Dead babies.", "Masturbation.", "Hormone injections.", "All-you-can-eat shrimp for $4.99.", "Incest.",
               "Scalping.", "Soup that is too hot.", "The &Uuml;bermensch.", "Nazis.", "Tom Cruise.",
               "Stifling a giggle at the mention of Hutus and Tutsis.", "Edible underpants.", "The Hustle.",
               "A Super Soaker&trade; full of cat pee.", "Figgy pudding.", "Object permanence.", "Consultants.",
               "Intelligent design.", "Nocturnal emissions.", "Uppercuts.", "Being marginalized.",
               "The profoundly handicapped.", "Obesity.", "Chutzpah.", "Unfathomable stupidity.", "Repression.",
               "Attitude.", "Passable transvestites.", "Party poopers.", "The American Dream", "Child beauty pageants.",
               "Puberty.", "Testicular torsion.", "The folly of man.", "Nickelback.", "Swooping.", "Goats eating cans.",
               "The KKK.", "Kamikaze pilots.", "Horrifying laser hair removal accidents.", "Adderall&trade;.",
               "A look-see.", "Doing the right thing.", "The taint; the grundle; the fleshy fun-bridge.", "Lactation.",
               "Pabst Blue Ribbon.", "Powerful thighs.", "Saxophone solos.", "The gays.",
               "A middle-aged man on roller skates.", "A foul mouth.", "The thing that electrocutes your abs.",
               "Heteronormativity.", "Cuddling.", "Coat hanger abortions.", "A big hoopla about nothing.", "Boogers.",
               "A hot mess.", "Raptor attacks.", "My collection of high-tech sex toys.", "Fear itself.", "<i>Bees?</i>",
               "Getting drunk on mouthwash.", "Sniffing glue.", "Oversized lollipops.", "An icepick lobotomy.",
               "Being rich.", "Friends with benefits.", "Teaching a robot to love.", "Women's suffrage.", "Me time.",
               "The heart of a child.", "Smallpox blankets.", "The clitoris.", "John Wilkes Booth.",
               "The glass ceiling.", "Sarah Palin.", "Sexy pillow fights.", "Yeast.", "Full frontal nudity.",
               "Parting the Red Sea.", "A Bop It&trade;.", "Michael Jackson.", "Team-building exercises.",
               "Harry Potter erotica.", "Authentic Mexican cuisine.", "Frolicking.", "Sexting.", "Grandma.",
               "Not giving a shit about the Third World.", "Licking things to claim them as your own.", "Genghis Khan.",
               "The hardworking Mexican.", "RoboCop.", "My relationship status.", "Scrubbing under the folds.",
               "Porn Stars.", "Horse meat.", "Sunshine and rainbows.", "Expecting a burp and vomiting on the floor.",
               "Barack Obama.", "Spontaneous human combustion.", "Natural selection.", "Mouth herpes.",
               "Flash flooding.", "Goblins.", "A monkey smoking a cigar.", "Spectacular abs.", "A good sniff.",
               "Wiping her butt.", "The Three-Fifths compromise.", "Pedophiles.", "Doin' it in the butt.",
               "Being fabulous.", "Mathletes.", "Wearing underwear inside-out to avoid doing laundry.",
               "Nipple blades.", "An M. Night Shyamalan plot twist.", "A bag of magic beans.", "Vigorous jazz hands.",
               "A defective condom.", "Skeletor.", "Vikings.", "Leaving an awkward voicemail.", "Teenage pregnancy.",
               "Dead parents.", "Hot cheese.", "My sex life.", "A mopey zoo lion.", "Assless chaps.",
               "Riding off into the sunset.", "Lance Armstrong's missing testicle.", "Sweet, sweet vengeance.",
               "Genital piercings.", "Keg stands.", "Darth Vader.", "Viagra&copy;.", "Necrophilia.",
               "A really cool hat.", "Toni Morrison's vagina.", "An Oedipus complex.",
               "The Tempur-Pedic&copy; Swedish Sleep System&trade;.", "Preteens.", "Dick fingers.",
               "A cooler full of organs.", "Shapeshifters.", "The Care Bear Stare.", "Erectile dysfunction.",
               "Keanu Reeves.", "The Virginia Tech Massacre.", "The Underground Railroad.", "The chronic.", "Queefing.",
               "Heartwarming orphans.", "A thermonuclear detonation.", "Cheating in the Special Olympics.",
               "Tangled Slinkys.", "A moment of silence.", "Civilian casualties.", "Catapults.", "Sharing needles.",
               "Ethnic cleansing.", "Emotions.", "Children on leashes.", "Balls.", "Homeless people.",
               "Eating all of the cookies before the AIDS bake-sale.", "Old-people smell.", "Farting and walking away.",
               "The inevitable heat death of the universe.", "The violation of our most basic human rights.",
               "Fingering.", "The placenta.", "The Rev. Dr. Martin Luther King, Jr.", "Leprosy.", "Sperm whales.",
               "Multiple stab wounds.", "Flightless birds.", "Grave robbing.",
               "Home video of Oprah sobbing into a Lean Cuisine&copy;.", "Oompa-Loompas.", "A murder most foul.",
               "Tentacle porn.", "Daddy issues.", "Bill Nye the Science Guy.", "Peeing a little bit.",
               "The miracle of childbirth.", "Tweeting.", "Another goddamn vampire movie.", "Britney Spears at 55.",
               "New Age music.", "The Make-A-Wish&reg; Foundation.",
               "Firing a rifle into the air while balls deep in a squealing hog.", "Active listening.", "Nicolas Cage.",
               "72 virgins.", "Stranger danger.", "Hope.", "A gassy antelope.", "BATMAN!!!", "Chivalry.",
               "Passing a kidney stone.", "Black people.", "Natalie Portman.", "A mime having a stroke.",
               "Classist undertones.", "Sean Penn.", "A mating display.", "The Holy Bible.", "Hot Pockets&copy;.",
               "A sad handjob.", "Pulling out.", "Serfdom.", "Pixelated bukkake.",
               "Dropping a chandelier on your enemies and riding the rope up.", "Jew-fros.", "Waiting 'til marriage.",
               "Euphoria&trade; by Calvin Klein.", "The World of Warcraft.", "Lunchables&trade;.", "The Kool-Aid Man.",
               "The Trail of Tears.", "Self-loathing.", "A falcon with a cap on its head.",
               "Historically black colleges.", "Not reciprocating oral sex.", "Global warming.", "Ghosts.",
               "World peace.", "A can of whoop-ass.", "The Dance of the Sugar Plum Fairy.",
               "A zesty breakfast burrito.", "Switching to Geico&reg;.", "Aaron Burr.",
               "Picking up girls at the abortion clinic.", "Land mines.", "Former President George W. Bush.", "Geese.",
               "Mutually-assured destruction.", "College.", "Date rape.", "Bling.",
               "A gentle caress of the inner thigh.", "A time travel paradox.", "Seppuku.", "Poor life choices.",
               "Waking up half-naked in a Denny's parking lot.", "Italians.", "GoGurt&reg;.", "Finger painting.",
               "Robert Downey, Jr.", "My soul.", "Smegma.", "Embryonic stem cells.", "The South.",
               "Christopher Walken.", "Gloryholes.", "Pretending to care.", "Public ridicule.", "A tiny horse.",
               "Arnold Schwarzenegger.", "A stray pube.", "Jerking off into a pool of children's tears.",
               "Child abuse.",
               "Glenn Beck convulsively vomiting as a brood of crab spiders hatches in his brain and erupts from his tear ducts.",
               "Menstruation.", "A sassy black woman.", "Re-gifting.", "Penis envy.", "A sausage festival.",
               "Getting really high.", "Drinking alone.", "Too much hair gel.", "Hulk Hogan.", "Overcompensation.",
               "Foreskin.", "Free samples.", "Shaquille O'Neal's acting career.", "Five-Dollar Footlongs&trade;.",
               "Whipping it out.", "A snapping turtle biting the tip of your penis.", "Muhammad (Praise Be Unto Him).",
               "Half-assed foreplay.", "Dental dams.", "Being a dick to children.", "Famine.", "Chainsaws for hands.",
               "A gypsy curse.", "AXE Body Spray.", "The Force.", "Explosions.", "Cybernetic enhancements.",
               "Customer service representatives.", "White privilege.", "Gandhi.", "Road head.", "God.",
               "Poorly-timed Holocaust jokes.", "8 oz. of sweet Mexican black-tar heroin.", "Judge Judy.",
               "The Little Engine That Could.", "Altar boys.", "Mr. Clean, right behind you.",
               "Vehicular manslaughter.", "Dwarf tossing.", "Friction.", "Lady Gaga.", "Scientology.", "Justin Bieber.",
               "A death ray.", "Vigilante justice.", "The Pope.", "A sea of troubles.", "Alcoholism.", "Poor people.",
               "A fetus.", "Women in yogurt commercials.", "Exactly what you'd expect.", "Flesh-eating bacteria.",
               "My genitals.", "A balanced breakfast.", "Dick Cheney.", "Lockjaw.", "Natural male enhancement.",
               "Take-backsies.", "Winking at old people.", "Opposable thumbs.", "Flying sex snakes.",
               "Passive-aggressive Post-it notes.", "Inappropriate yodeling.", "Golden showers.", "Racism.",
               "Copping a feel.", "Auschwitz.", "Elderly Japanese men.", "Raping and pillaging.",
               "Kids with ass cancer.", "Pictures of boobs.", "The homosexual agenda.",
               "A homoerotic volleyball montage.", "Sexual tension.", "Hurricane Katrina.", "Fiery poops.", "Science.",
               "Dry heaving.", "Cards Against Humanity.", "Fancy Feast&copy;.", "A bleached asshole.",
               "Lumberjack fantasies.", "American Gladiators.", "Autocannibalism.", "Sean Connery.", "William Shatner.",
               "Domino's&trade; Oreo&trade; Dessert Pizza.", "An asymmetric boob job.", "Centaurs.", "A micropenis.",
               "Asians who aren't good at math.", "The milk man.", "Waterboarding.", "Wifely duties.", "Loose lips.",
               "The Blood of Christ.", "Actually taking candy from a baby.", "The token minority.", "Jibber-jabber.",
               "A brain tumor.", "Bingeing and purging.", "A clandestine butt scratch.", "The Chinese gymnastics team.",
               "Prancing.", "The Hamburglar.", "Police brutality.", "Man meat.", "Forgetting the Alamo.",
               "Eating the last known bison.", "Crystal meth.", "Booby-trapping the house to foil burglars.",
               "My inner demons.", "Third base.", "Soiling oneself.", "Laying an egg.", "Giving 110%.", "Hot people.",
               "Friendly fire.", "Count Chocula.", "Pac-Man uncontrollably guzzling cum.", "Estrogen.", "My vagina.",
               "Kanye West.", "A robust mongoloid.", "The Donald Trump Seal of Approval&trade;.",
               "The true meaning of Christmas.", "Her Royal Highness, Queen Elizabeth II.",
               "An honest cop with nothing left to lose.", "Feeding Rosie O'Donnell.", "The Amish.", "The terrorists.",
               "When you fart and a little bit comes out.", "Pooping back and forth. Forever.",
               "Friends who eat all the snacks.", "Cockfights.", "Bitches.", "Seduction.", "A big black dick.",
               "A beached whale.", "A bloody pacifier.", "A crappy little hand.", "A low standard of living.",
               "A nuanced critique.", "Panty raids.", "A passionate Latino lover.", "A rival dojo.", "A web of lies.",
               "A woman scorned.", "Clams.", "Apologizing.", "A plunger to the face.", "Neil Patrick Harris.",
               "Beating your wives.", "Being a dinosaur.", "Shaft.", "Bosnian chicken farmers.", "Nubile slave boys.",
               "Carnies.", "Coughing into a vagina.", "Suicidal thoughts.", "The ooze.", "Deflowering the princess.",
               "Dorito breath.", "Eating an albino.", "Enormous Scandinavian women.", "Fabricating statistics.",
               "Finding a skeleton.", "Gandalf.", "Genetically engineered super-soldiers.", "George Clooney's musk.",
               "Getting abducted by Peter Pan.", "Getting in her pants, politely.", "Gladiatorial combat.",
               "Clenched butt cheeks.", "Hipsters.", "Historical revisionism.", "Insatiable bloodlust.", "Jafar.",
               "Jean-Claude Van Damme.", "Just the tip.", "Mad hacky-sack skills.", "Leveling up.",
               "Literally eating shit.", "Making the penises kiss.", "24-hour media coverage.",
               "Medieval Times&copy; Dinner & Tournament.", "Moral ambiguity.", "My machete.",
               "One thousand Slim Jims.", "Ominous background music.", "Overpowering your father.",
               "Stockholm Syndrome.", "Quiche.", "Quivering jowls.", "Revenge fucking.",
               "Ripping into a man's chest and pulling out his still-beating heart.",
               "Ryan Gosling riding in on a white horse.", "Santa Claus.", "Scrotum tickling.", "Sexual humiliation.",
               "Sexy Siamese twins.", "Saliva.", "Space muffins.", "Statistically validated stereotypes.",
               "Sudden Poop Explosion Disease.", "The boners of the elderly.", "The economy.", "Syphilitic insanity.",
               "The Gulags.", "The harsh light of day.", "The hiccups.", "The shambling corpse of Larry King.",
               "The four arms of Vishnu.", "Being a busy adult with many important things to do.", "Tripping balls.",
               "Words, words, words.", "Zeus's sexual appetites.", "A bigger, blacker dick.",
               "The mere concept of Applebee's&reg;.", "A sad fat dragon with no friends.",
               "Catastrophic urethral trauma.", "Hillary Clinton's death stare.", "Existing.",
               "A pinata full of scorpions.", "Mooing.", "Swiftly achieving orgasm.", "Daddy's belt.",
               "Double penetration.", "Weapons-grade plutonium.", "Some really fucked-up shit.",
               "Subduing a grizzly bear and making her your wife.", "Rising from the grave.",
               "The mixing of the races.",
               "Taking a man's eyes and balls out and putting his eyes where his balls go and then his balls in the eye holes.",
               "Scrotal frostbite.", "All of this blood.", "Loki, the trickster god.", "Whining like a little bitch.",
               "Pumping out a baby every nine months.", "Tongue.", "Finding Waldo.",
               "Upgrading homeless people to mobile hotspots.", "Wearing an octopus for a hat.",
               "An unhinged ferris wheel rolling toward the sea.", "Living in a trashcan.", "The corporations.",
               "A magic hippie love cloud.", "Fuck Mountain.", "Survivor's guilt.", "Me.",
               "Getting hilariously gang-banged by the Blue Man Group.", "Jeff Goldblum.", "Making a friend.",
               "A soulful rendition of &#34;Ol' Man River.&#34;", "Intimacy problems.",
               "A sweaty, panting leather daddy.", "Spring break!", "Being awesome at sex.",
               "Dining with cardboard cutouts of the cast of &#34;Friends.&#34;", "Another shot of morphine.",
               "Beefin' over turf.", "A squadron of moles wearing aviator goggles.", "Bullshit.", "The Google.",
               "Pretty Pretty Princess Dress-Up Board Game&#174;.", "The new Radiohead album.", "An army of skeletons.",
               "A man in yoga pants with a ponytail and feather earrings.", "Mild autism.", "Nunchuck moves.",
               "Whipping a disobedient slave.", "An ether-soaked rag.", "A sweet spaceship.",
               "A 55-gallon drum of lube.", "Special musical guest, Cher.", "The human body.",
               "Boris the Soviet Love Hammer.", "The grey nutrient broth that sustains Mitt Romney.", "Tiny nipples.",
               "Power.", "Oncoming traffic.", "A dollop of sour cream.", "A slightly shittier parallel universe.",
               "My first kill.", "Graphic violence, adult language, and some sexual content.",
               "Fetal alcohol syndrome.", "The day the birds attacked.", "One Ring to rule them all.",
               "Grandpa's ashes.", "Basic human decency.", "A Burmese tiger pit.", "Death by Steven Seagal",
               "Dragon boobs.", "Verisimilitude.", "Dissociated mechanics.", "Rape.", "Storygames.", "Random chargen",
               "RPG.net.", "Dice inserted somewhere painful.", "FATAL.", "Ron Edwards' brain damage.",
               "Boob plate armor.", "Gamer chicks.", "GNS theory.", "Drizzt.",
               "The entire Palladium Books&reg; Megaverse&trade;", "BadWrongFun.", "Misogynerds.", "Cultural Marxism.",
               "Pissing on Gary Gygax's grave.", "Steve Jackson's beard.", "Natural 20.", "Rapenards.",
               "The Crisis of Treachery&trade;.", "Game balance.", "Fishmalks.", "A kick to the dicebags.",
               "Bearded dwarven women.", "Owlbear's tears.", "Magic missile.", "THAC0.", "Bigby's Groping Hands.",
               "Drow blackface.", "Save or die.", "Swine.", "The Forge.", "Healing Surges.", "Gelatinous Cubes.",
               "Total Party Kill.", "Quoting Monty Python.", "Dumbed down shit for ADD WoW babies.", "Mike Mearls.",
               "Comeliness.", "Vampire: The Masquerade.", "Rifts&trade;.", "The random prostitute table.",
               "Dildo of Enlightenment +2", "Grognards Against Humanity.", "Cthulhu.",
               "The naked succubus in the Monster Manual.", "Role-playing and roll-playing.", "Fun Tyrant.", "4rries.",
               "Martial dailies.", "Black Tokyo.", "Killfuck Soulshitter.", "Cheetoism.", "Grimdark.", "Kobolds.",
               "Oozemaster.", "Rocks fall, everyone dies.", "Mark Rein&middot;Hagen.", "Maid RPG.",
               "Splugorth blind warrior women.", "Dying during chargen.", "Slaughtering innocent orc children.",
               "Lesbian stripper ninjas.", "Magical tea party.", "Grinding levels.", "Dice animism.",
               "White privilege.", "Githyanki therapy.", "Amber Diceless Roleplaying.",
               "A ratcatcher with a small but vicious dog.", "Bribing the GM with sexual favors.",
               "Eurocentric fantasy.", "Sacred cows.", "Gygaxian naturalism.", "Special snowflakes.", "Neckbeards.",
               "Gazebos.", "Lorraine Williams.", "Nude larping.", "Portable holes.", "Steampunk bullshit.",
               "Dump stats.", "Ale and whores.", "Japanese schoolgirl porn.", "Horny catgirls.", "Japanese people.",
               "Cimo.", "ZA WARUDO!", "40 gigs of lolicon.", "Goku's hair.", "Slashfic.", "Star Gentle Uterus",
               "Naruto headbands.", "Homestuck troll horns.", "Hayao Miyazaki.", "The tsunami.", "Death Note.",
               "Small breasts.", "Asians being racist against each other.", "Weeaboo bullshit.", "Tsundere.",
               "Body pillows.", "A lifelike silicone love doll.", "Anime figures drenched in jizz.", "Surprise sex.",
               "Yaoi.", "Girls with glasses.", "Bronies.", "Blue and white striped panties.", "4chan.",
               "Hello Kitty vibrator.", "Finishing attack.", "Keikaku* *(keikaku means plan).",
               "Hatsune Miku's screams.", "School swimsuits.", "Lovingly animated bouncing boobs.", "Dragon Balls.",
               "Zangief's chest hair.", "DeviantArt.", "Giant fucking robots.", "Crossplay.", "Moeblob.",
               "Carl Macek's rotting corpse.", "My waifu.", "Voice actress Megumi Hayashibara.", "Lynn Minmei.",
               "Panty shots.", "Love and Justice.", "Consensual tentacle rape.", "Gundam.",
               "Captain Bright slapping Amuro.", "The Wave Undulation Cannon.",
               "Having sex in the P.E. equipment shed.", "Tainted sushi.", "Shitty eurobeat music.", "Bad dubbing.",
               "Fangirls.", "Kawaii desu uguu.", "Futanari.", "Lesbian schoolgirls.",
               "Osamu Tezuka, rolling in his grave forever.", "FUNimation.", "Underage cosplayers in bondage gear.",
               "Jackie Chan.", "Exchanging Pocky for sexual favors.", "Shipping.", "Chiyo's father.", "Magikarp.",
               "Derpy.", "Nanoha and her special friend Fate.", "The marbles from Ramune bottles.", "Wideface.",
               "Spoilers.", "Man-Faye.", "Oppai mousepads.", "Another dimension.", "Homura sniffing Madoka's panties.",
               "Hadouken.", "Asian ball-jointed dolls.", "J-list.", "Childhood friends.",
               "Monkey D. Luffy's rubbery cock.", "Cloud's giant fucking Buster Swords.",
               "Taking a dump in Char's helmet.", "Hentai marathons.", "Gothic Lolita.", "Onaholes.",
               "Super Saiyan Level 2.", "Gaia Online.", "Santa's heavy sack.",
               "Clearing a bloody path through Walmart with a scimitar.", "Another shitty year.",
               "Whatever Kwanzaa is supposed to be about.", "A Christmas stocking full of coleslaw.", "Elf cum.",
               "The tiny, calloused hands of the Chinese children that made this card.",
               "Taking down Santa with a surface-to-air missile.", "Socks.", "Pretending to be happy.",
               "Krampus, the Austrian Christmas monster.", "The Star Wars Holiday Special.", "My hot cousin.",
               "Mall Santa.", "Several intertwining love stories featuring Hugh Grant.",
               "A Hungry-Man&trade; Frozen Christmas Dinner for one.", "Gift-wrapping a live hamster.",
               "Space Jam on VHS.", "Immaculate conception.", "Fucking up 'Silent Night' in front of 300 parents.",
               "A visually arresting turtleneck.", "A toxic family environment.", "Eating an entire snowman.",
               "Bumpses.", "A Vin Gerard H8 X 10.", "Harry Acropolis.", "Under the ring.", "Afa The Wild Samoan.",
               "Peanut Butter and Baby sandwiches.", "Yard Tards.", "Two girls, one cup.", "Ugly Mexican Hookers.",
               "Duct tape.", "Sodaj.", "Steve The Teacher.", "Jefferee.", "Autoerotic Asphyxiation.",
               "Sonic The Hedgehog.", "Lotto Money.", "Jailbait.", "Prison rape.", "Two And A Half Men.", "Anne Frank.",
               "Black Santa.", "Jesus Christ (our lord and saviour).", "Farting with your armpits.", "Poopsicles.",
               "Slaughtering innocent children.", "Sex with vegetables.", "My gay ex-husband.",
               "Accidentally sexting your mom.", "Tabasco in your pee-hole.", "Pee Wee Herman.",
               "A breath of fresh air.", "A great big floppy donkey dick.", "A pyramid scheme.",
               "A school bus surrounded by cop cars.", "A short walk in the desert with shovels.",
               "All the boys staring at your chest.", "An amorous stallion.", "Being so wet it just slides out of you.",
               "Being tarred and feathered.", "Catching 'em all.",
               "Chained to the bed and whipped to orgasmic bliss by a leather-clad woman.", "Child-bearing hips.",
               "Defenestration.", "Dungeons and/or dragons.", "Ecco the Dolphin.",
               "George Washington riding on a giant eagle.", "Getting abducted and probed by aliens.",
               "Going viral on YouTube.", "Gushing.", "Making the baby Jesus cry.", "More than you can chew.",
               "Napalm.", "Pancake bitches.", "Playing God with the power of lightning.", "Playing tonsil-hockey.",
               "Racing cheese wheels downhill.", "Riding the bomb.", "Settling arguments with dance-offs.",
               "Sheer spite.", "Sinister laughter.", "SS Girls.", "Stealing your sister's underwear.",
               "Stroking a cat the wrong way.", "Sucking and blowing.", "The bullet with your name on it.",
               "The entire rest of eternity, spent in fucking Bruges.", "The oceans rising to reclaim the land.",
               "A cocained-fuelled sex orgy heart attack.", "A cocktail umbrella", "A murder/suicide pact.",
               "A squirming mass of kittens.", "An angry mob with torches and pitchforks.",
               "Biting my girlfriend like a vampire during sex.", "Dropping your pants and saluting.",
               "Frankenstein's Monster", "Getting a blowjob in a theater.", "Going full retard.",
               "Going slob-slob-slob all over that knob.", "Leaking implants.", "Low-flying planes.",
               "Monkies flinging their own shit.", "My robot duplicate.", "Other people’s children.",
               "People who can't take a joke. Seriously.", "Popping a boner during Sex Ed class.",
               "Projectile vomiting.", "Pulling down panties with your teeth.", "Saying", "Shedding skin like a snake.",
               "Shooting Valley Girls for like, saying like all the time. Really.", "Slow seductive tentacle rape.",
               "Talking like a pirate, y’arr!", "Tenderly kissing a unicorn's horn.", "That bastard Jesus!",
               "The last shreads of dignity.", "The power of friendship.", "This card intentionally left blank.",
               "Throwing water on a braless woman in a white t-shirt", "Upskirts.",
               "Wasting all your money on hookers and booze.", "Winning.", "A foot fetish.", "A powerful gag reflex.",
               "A tight, Asian pussy.", "Explosive decompression.", "Extraordinary Rendition.",
               "Forgetting the safety word.", "Greeting Christmas carollers naked.", "Handcuffs, without the key.",
               "Having a drill for a penis.", "Hot Jailbait Ass.", "Liposuction gone horrible wrong.",
               "My harem of scantily clad women.", "Nazi Zombie Robot Ninjas.", "Redneck gypsies.", "Scissoring.",
               "A guy and two robots who won’t shut up.", "A shotgun wedding.", "Anne Frank's diary",
               "Autoerotic asphyxiation.", "Blow Up Bianca the Latex Lovedoll.",
               "Endlessly tumbling down an up escalator.", "Fun with nuns.", "Getting it all over the walls.",
               "Holiday Dinner by Jack Daniels.", "Nailgun fights.", "Teaching the bitch a lesson.",
               "Nazi super science.", "Making a human centipede.",
               "The primal, ball-slapping sex your parents are having right now.",
               "A cat video so cute that your eyes roll back and your spine slides out of your anus.", "Cock.",
               "A cop who is also a dog.", "Dying alone and in pain.", "Gay aliens.", "The way white people is.",
               "Reverse cowgirl.", "The Quesadilla Explosion Salad&trade; from Chili's&copy;.",
               "Actually getting shot, for real.", "Not having sex.", "Vietnam flashbacks.",
               "Running naked through a mall, pissing and shitting everywhere.", "Nothing.",
               "Warm, velvety muppet sex.", "Self-flagellation.",
               "The systematic destruction of an entire people and their way of life.", "Samuel L. Jackson.",
               "A boo-boo.", "Going around punching people.", "The entire Internet.", "Some kind of bird-man.",
               "Chugging a lava lamp.", "Having sex on top of a pizza.", "Indescribable loneliness.",
               "An ass disaster.", "Shutting the fuck up.", "All my friends dying.",
               "Putting an entire peanut butter and jelly sandwich into the VCR.", "Spending lots of money.",
               "Some douche with an acoustic guitar.", "Flying robots that kill people.",
               "A greased-up Matthew McConaughey.", "An unstoppable wave of fire ants.",
               "Not contributing to society in any meaningful way.",
               "An all-midget production of Shakespeare's Richard III.", "Screaming like a maniac.",
               "The moist, demanding chasm of his mouth.", "Filling every orifice with butterscotch pudding.",
               "Unlimited soup, salad, and breadsticks.", "Crying into the pages of Sylvia Plath.", "Velcro&trade;.",
               "A PowerPoint presentation.", "A surprising amount of hair.",
               "Eating Tom Selleck's mustache to gain his powers.", "Roland the Farter, flatulist to the king.",
               "That ass.", "A pile of squirming bodies.", "Buying the right pants to be cool.", "Blood farts.",
               "Three months in the hole.", "A botched circumcision.", "The Land of Chocolate.",
               "Slapping a racist old lady.", "A lamprey swimming up the toilet and latching onto your taint.",
               "Jumping out at people.", "A black male in his early 20s, last seen wearing a hoodie.",
               "Mufasa's death scene.", "Bill Clinton, naked on a bearskin rug with a saxophone.",
               "Demonic possession.", "The Harlem Globetrotters.", "Vomiting mid-blowjob.", "My manservant, Claude.",
               "Having shotguns for legs.", "Letting everyone down.", "A spontaneous conga line.",
               "A vagina that leads to another dimension.", "Disco fever.",
               "Getting your dick stuck in a Chinese finger trap with another dick.", "Fisting.",
               "The thin veneer of situational causality that underlies porn.", "Girls that always be textin'.",
               "Blowing some dudes in an alley.",
               "Drinking ten 5-hour ENERGYs&reg; to get fifty continuous hours of energy.",
               "Sneezing, farting, and coming at the same time.", "A freshly-filled diaper", "Glue",
               "An unusually-attractive transvestite", "Hand-me-down adult diapers", "A stillborn fetus",
               "A disgraced pelican", "Three buckets of urine, free for 2 nights, with no late fee", "My testicles",
               "A black woman's vagina", "My asshole", "A whale's blowhole", "2 Girls 1 Cup",
               "The Big Bang Theory (TV)", "Teen pregnancy", "Ass hair", "Vaginal warts", "Ellen Degeneres",
               "Jews Against Humanity", "Indy wrestling", "Cunt",
               "Beating a crowd of delightful parents to death with a steel dildo",
               "Beating a crowd of delightful parents to death with a steel dildo while dressed as Ru Paul's brother, Ron.",
               "A roll in the hay", "Get 'em, Steve-Dave!", "God Hates You", "Manboobs.", "Daniel Benoit",
               "Vomiting in the shower", "An intellectually superior overlord", "Dwight Schrute", "Casey Anthony",
               "Clubbin seals", "Stunt cock", "Anal lice", "Lightsaber Dildos"]
MatureBlackCards = ["_? There's an app for that.", "Why can't I sleep at night?", "What's that smell?",
               "I got 99 problems but _ ain't one.", "Maybe she's born with it. Maybe it's _.",
               "What's the next Happy Meal&copy; toy?",
               "Anthropologists have recently discovered a primitive tribe that worships _.",
               "It's a pity that kids these days are all getting involved with _.",
               "During Picasso's often-overlooked Brown Period, he produced hundreds of paintings of _.",
               "Alternative medicine is now embracing the curative powers of _.",
               "What's that sound?", "What ended my last relationship?",
               "MTV's new reality show features eight washed-up celebrities living with _.", "I drink to forget _.",
               "I'm sorry professor, but I couldn't complete my homework because of _.",
               "What is Batman's guilty pleasure?",
               "This is the way the world ends, not with a bang but with _.",
               "What's a girl's best friend?", "TSA guidelines now prohibit _ on airplanes.",
               "_. That's how I want to die.",
               "In the new Disney Channel Original Movie, Hannah Montana struggles with _ for the first time.",
               "What does Dick Cheney prefer?",
               "Dear Abby, I'm having some trouble with _ and would like your advice.",
               "Instead of coal, Santa now gives the bad children _.", "What's the most emo?",
               "In 1,000 years when paper money is but a distant memory, _ will be our currency.",
               "What's the next superhero/sidekick duo?",
               "In M. Night Shyamalan's new movie, Bruce Willis discovers that _ had really been _ all along.",
               "A romantic, candlelit dinner would be incomplete without _.", "_. Becha can't have just one!",
               "White people like _.", "_. High five, bro.",
               "Next from J.K. Rowling: Harry Potter and the Chamber of _.", "BILLY MAYS HERE FOR _.",
               "War! What is it good for?",
               "During sex, I like to think about _.", "What are my parents hiding from me?",
               "What will always get you laid?", "In L.A. County Jail, word is you can trade 200 cigarettes for _.",
               "What did I bring back from Mexico?", "What don't you want to find in your Chinese food?",
               "What will I bring back in time to convince people that I am a powerful wizard?",
               "How am I maintaining my relationship status?", "_. It's a trap!",
               "Coming to Broadway this season, _: The Musical.",
               "While the United States raced the Soviet Union to the moon, the Mexican government funneled millions of pesos into research on _.",
               "After the earthquake, Sean Penn brought _ to the people of Haiti.",
               "Next on ESPN2, the World Series of _.",
               "But before I kill you, Mr. Bond, I must show you _.", "What gives me uncontrollable gas?",
               "What do old people smell like?", "The class field trip was completely ruined by _.",
               "When Pharaoh remained unmoved, Moses called down a Plague of _.", "What's my secret power?",
               "What's there a ton of in heaven?", "What would grandma find disturbing, yet oddly charming?",
               "What did the U.S. airdrop to the children of Afghanistan?", "What helps Obama unwind?",
               "What did Vin Diesel eat for dinner?", "_: good to the last drop.", "Why am I sticky?",
               "What gets better with age?", "_: kid-tested, mother-approved.", "What's the crustiest?",
               "What's Teach for America using to inspire inner city students to succeed?",
               "Studies show that lab rats navigate mazes 50% faster after being exposed to _.",
               "Life for American Indians was forever changed when the White Man introduced them to _.",
               "Make a haiku.",
               "I do not know with what weapons World War III will be fought, but World War IV will be fought with _.",
               "Why do I hurt all over?", "What am I giving up for Lent?",
               "In Michael Jackson's final moments, he thought about _.",
               "In an attempt to reach a wider audience, the Smithsonian Museum of Natural History has opened an interactive exhibit on _.",
               "When I am President of the United States, I will create the Department of _.",
               "When I am a billionaire, I shall erect a 50-foot statue to commemorate _.", "What never fails to liven up the party?",
               "What's the new fad diet?", "Major League Baseball has banned _ for giving players an unfair advantage.",
               "My plan for world domination begins with _.",
               "The CIA now interrogates enemy agents by repeatedly subjecting them to _.",
               "In Rome, there are whisperings that the Vatican has a secret room devoted to _.",
               "Science will never explain _.", "When all else fails, I can always masturbate to _.",
               "I learned the hard way that you can't cheer up a grieving friend with _.",
               "In its new tourism campaign, Detroit proudly proclaims that it has finally eliminated _.",
               "The socialist governments of Scandinavia have declared that access to _ is a basic human right.",
               "In his new self-produced album, Kanye West raps over the sounds of _.",
               "What's the gift that keeps on giving?",
               "Next season on Man vs. Wild, Bear Grylls must survive in the depths of the Amazon with only _ and his wits.",
               "When I pooped, what came out of my butt?",
               "In the distant future, historians will agree that _ marked the beginning of America's decline.",
               "What has been making life difficult at the nudist colony?",
               "And I would have gotten away with it, too, if it hadn't been for _.",
               "What brought the orgy to a grinding halt?", "During his midlife crisis, my dad got really into _.",
               "My new favorite porn star is Joey &#34;_&#34; McGee.",
               "Before I run for president, I must destroy all evidence of my involvement with _.",
               "This is your captain speaking. Fasten your seatbelts and prepare for _.",
               "In his newest and most difficult stunt, David Blaine must escape from _.",
               "The Five Stages of Grief: denial, anger, bargaining, _, and acceptance.",
               "Members of New York's social elite are paying thousands of dollars just to experience _.",
               "This month's Cosmo: &#34;Spice up your sex life by bringing _ into the bedroom.&#34;",
               "Little Miss Muffet Sat on a tuffet, Eating her curds and _.",
               "My country, 'tis of thee, sweet land of _.",
               "After months of debate, the Occupy Wall Street General Assembly could only agree on &#34;More _!&#34;",
               "Next time on Dr. Phil: How to talk to your child about _.",
               "Only two things in life are certain: death and _.",
               "Everyone down on the ground! We don't want to hurt anyone. We're just here for _.",
               "The healing process began when I joined a support group for victims of _.",
               "The votes are in, and the new high school mascot is _.",
               "Charades was ruined for me forever when my mom had to act out _.",
               "Tonight on 20/20: What you don't know about _ could kill you.",
               "You haven't truly lived until you've experienced _ and _ at the same time.",
               "D&D 4.0 isn't real D&D because of the _.", "It's a D&D retroclone with _ added.",
               "Storygames aren't RPGs because of the _.", "The Slayer's Guide to _.", "Alightment: Chaotic _",
               "It's a D&D retroclone with _ added.", "What made the paladin fall? _",
               "The portal leads to the quasi-elemental plane of _.", "The Temple of Elemental _.",
               "Pathfinder is basically D&D _ Edition.", "_ : The Storytelling Game.",
               "People are wondering why Steve Jackson published GURPS _.", "Linear Fighter, Quadratic _.",
               "You start with 1d4 _ points.",
               "Back when I was 12 and I was just starting playing D&D, the game had _.", "Big Eyes, Small _.",
               "In the grim darkness of the future there is only _.", "My innovative new RPG has a stat for _.",
               "A true gamer has no problem with _.", "Elminster cast a potent spell and then had sex with _.",
               "The Deck of Many _.", "You are all at a tavern when _ approach you.",
               "For the convention I cosplayed as Sailor Moon, except with _.",
               "The worst part of Grave of the Fireflies is all the _.",
               "In the Evangelion remake, Shinji has to deal with _.", "Worst anime convention purchase ever? _.",
               "While powering up Vegeta screamed, _!", "You evaded my _ attack. Most impressive.",
               "The magical girl found out that the Power of Love is useless against _.",
               "The Japanese government has spent billions of yen researching _.", "_ is Best Pony.", "The _ of Haruhi Suzumiya.",
               "The new thing in Akihabara is fetish cafes where you can see girls dressed up as _.",
               "Your drill can pierce _!", "Avatar: The Last _ bender.",
               "In the name of _ Sailor Moon will punish you!", "No harem anime is complete without _.",
               "My boyfriend's a _ now.", "_.tumblr.com",
               "Somehow they made a cute mascot girl out of _.",
               "Haruko hit Naoto in the head with her bass guitar and _ came out.",
               "After blacking out during New year's Eve, I was awoken by _.",
               "This holiday season, Tim Allen must overcome his fear of _ to save Christmas.", "Jesus is _.",
               "Every Christmas, my uncle gets drunk and tells the story about _.",
               "What keeps me warm during the cold, cold, winter?",
               "On the third day of Christmas, my true love gave to me: three French hens, two turtle doves, and _.",
               "Wake up, America. Christmas is under attack by secular liberals and their _.",
               "We got the third rope, now where's the fourth?",
               "Tackle, Dropdown, _.", "Christopher Daniels is late on his _.",
               "Genius is 10% inspiration, 90% _.",
               "The best thing I ever got for Christmas was _.",
               "There's no crying in _.", "Mastodon! Pterodactyl! Triceratops! Sabretooth Tiger! _!",
               "Don't eat the _.", "SOOOOO hot, want to touch the _.",
               "Stop looking at me _!", "I'm cuckoo for _ puffs.", "Silly rabbit, _ are for kids.",
               "Between love and madness lies _.",
               "Instead of chess, the Grim Reaper now gambles for your soul with a game of _.",
               "Why is my throat sore?",
               "I’m very sorry Mrs. Smith, but Little Billy has tested positive for _.",
               "Instead of beating them, Chris Brown now does _ to women.",
               "Instead of cutting, trendy young emo girls now engage in _.",
               "The definition of rock bottom is gambling away _.",
               "The Mayan prophecies really heralded the coming of _ in 2012.",
               "The next US election will be fought on the key issues of _.",
               "When I was 10 I wrote to Santa wishing for _.", "Where or How I met my last signifigant other: _.",
               "_, Never leave home without it.", "_. This is my fetish.", "I did _ so you don't have to!",
               "I need your clothes, your bike, and _.",
               "In a new Cold War retro movie, the red menace tries to conquer the world through the cunning use of _.",
               "My zombie survival kit includes food, water, and _.", "The way to a man's heart is through _.",
               "What was the theme of my second wedding?", "What's the newest Japanese craze to head West?",
               "Everybody loves _.", "I can only express myself through _.",
               "My new porn DVD was completely ruined by the inclusion of _", "The latest horrifying school shooting was inspired by _.",
               "I got fired because of my not-so-secret obsession over _.", "My new favourite sexual position is _",
               "A successful job interview begins with a firm handshake and ends with _.",
               "Lovin' you is easy 'cause you're _.", "My life is ruled by a vicious cycle of _.",
               "The blind date was going horribly until we discovered our shared interest in _.",
               "_. Awesome in theory, kind of a mess in practice.",
               "I'm not like the rest of you. I'm too rich and busy for _.",
               "In the seventh circle of Hell, sinners must endure _ for all eternity.",
               "_: Hours of fun. Easy to use. Perfect for _!", "What left this stain on my couch?",
               "Call the law offices of Goldstein & Goldstein, because no one should have to tolerate _ in the workplace.",
               "When you get right down to it, _ is just _.",
               "Turns out that _-Man was neither the hero we needed nor wanted.",
               "As part of his daily regimen, Anderson Cooper sets aside 15 minutes for _.",
               "Money can't buy me love, but it can buy me _.", "With enough time and pressure, _ will turn into _.",
               "And what did you bring for show and tell?",
               "During high school, I never really fit in until I found _ club.",
               "Hey, baby, come back to my place and I'll show you _.",
               "To prepare for his upcoming role, Daniel Day-Lewis immersed himself in the world of _.",
               "Finally! A service that delivers _ right to your door.",
               "My gym teacher got fired for adding _ to the obstacle course.",
               "As part of his contract, Prince won't perform without _ in his dressing room.",
               "It's only _ if you get caught!",
               "_: The Next Generation", "Terminator 4: _", "Disney presents _ on ice!", "_. The other white meat.",
               "I love the smell of _ in the morning.",
               "You're not gonna believe this, but _.", "_. All the cool kids are doing it.",
               "Baskin Robbins just added a 32nd flavor: _!",
               "I can drive and ____ at the same time.", "_ ain't nothin' to fuck wit'!"]
CleanBlackCards = ["Papa, come quickly! There, in the garden!Do you see _____? Tell me you see it, Papa!",
     "Attention students! Principal Butthead is at home recovering from _____________. We hope he’ll be back soon.",
     "I’m sorry, Jordan, but that’s not an acceptable Science Fair project. That’s just _______.",
     "The warm August air was filled with change. Things were different, for Kayla was now ________________.",
     "This is gonna be the best sleepover ever. Once Mom goes to bed, it’s time for _________!",
     "Coming soon! Batman vs. ________________.",
     "Class, pay close attention. I will now demonstrate the physics of ________________.",
     "Hey Riley, I’ll give you five bucks if you try _________.",
     "Time to put on my favorite t-shirt, the one that says “I heart ________.”",
     "My dad and I enjoy _________________ together.",
     "Hey, kids. I’m Sensei Todd. Today, I’m gonna teach you how to defend yourself against _________.",
     "MY NAME CHUNGO. CHUNGO LOVE ________________.",
     "Never fear, Captain _________ is here!",
     "Kids, Dad is trying something new this week. It’s called “_____.”",
     "Oh, no thank you, Mrs. Lee. I’ve had plenty of _________________ for now.",
     "There’s nothing better than a peanut butter and _____________ sandwich.",
     "And over here is Picasso’s most famous painting, “Portrait of _____.”",
     "The aliens are here. They want ______.",
     "They call me “Mr. ___________.”",
     "CHUNGO FEEL SICK. CHUNGO NO LIKE _________________ ANYMORE.",
     "Mom!? You have to come pick me up! There’s __________ at this party!",
     "CNN breaking news! Over half of Americans are now ____________.",
     "On the next episode of Dora the Explorer, Dora explores ________________.",
     "Alright, which one of you little turds is responsible for _______________?!",
     "Ladies and gentlemen, I have discovered something amazing. I have discovered ________________.",
     "And in the blue corner, weighing in at 280 pounds, it’s Tommy “_____” Takahashi!",
     "Outback Steakhouse: No rules. Just ____________.",
     "Ew. Grandpa smells like ______.",
     "My name is Peter Parker. I was bitten by a radioactive spider, and now I’m _____________.",
     "Put on your helmet, strap on your goggles, and get ready for _____________!"
     "Attention students! This is Principal Butthead reminding you that we do not allow _____________ in the hallway.",
     "Thank you.	What’s about to take this school dance to the next level?",
     "Little Miss Muffet Sat on a tuffet Eating her curds and ____________.",
     "All I want for Christmas is ________________.",
     "Me and my friends don’t play with dolls anymore. We’re into _______ now.",
     "We’re not supposed to go in the attic. My parents keep _________________ in there.",
     "Police! Arrest this man! He’s ____________.",
     "My favorite dinosaur is “_______asaurus.”",
     "When I pooped, what came out of my butt?",
     "I’m not like the other children.",
     "Toys bore me, and I don’t care for sweets. I prefer _________.",
     "I’m sorry, Mrs. Sanchez, but I couldn’t finish my homework because of ________________.	",
     "Oh Dark Lord, we show our devotion with a humble offering of ______________!",
     "Thanks for watching! If you want to see more vids of __________, smash that subscribe.",
     "We’re off to see the wizard, the wonderful wizard of ______________!",
     "What’s all fun and games until somebody gets hurt?",
     "Young lady, we do not allow _________________ at the dinner table.",
     "Welcome! We’re glad you’re here. Now sit back, relax, and enjoy ________________.",
     "My favorite book is The Amazing Adventures of ________________.",
     "Well, look what we have here! A big fancy man walkin’ in like he’s ________________.",
     "ENOUGH! I will not let _________________ tear this family apart!",
     "Rub a dub dub, _________________ in a tub!",
     "Madam President, we’ve run out of time. The only option is ________.",
     "I have invented a new sport. I call it “___________ ball.”",
     "Hey, check out my band! We’re called “Rage Against _______________.”",
     "Moms love ______.",
     "Where do babies come from?",
     "CHUNGO ANGRY. CHUNGO DESTROY _______.",
     "At school, I’m just Mandy. But at summer camp, I’m “_____ Mandy.”",
     "James Bond will return in “No Time for _______________.”",
     "It’s BIG. It’s SCARY. It’s _____________!",
     "Disney proudly presents: “_________ on Ice.”",
     "What really killed the dinosaurs?",
     "Beep beep! _________________ coming through!",
     "Now in bookstores: Nancy Drew and the Mystery of ________________.",
     "You don’t love me, Sam. All you care about is ________________.",
     "Did you know that Benjamin Franklin invented ________________?",
     "One nation, under God, indivisible, with liberty and _________________ for all.",
     "The easiest way to tell me and my twin apart is that I have a freckle on my cheek and she’s ___________.",
     "Hey guys. I just want to tell all my followers who are struggling with ________________: it DOES get better.",
     "Whoa there, partner! Looks like _________________ spooked my horse.",
     "Princess Marigold, the kingdom is in danger! You must stop ________________.",
     "Shut up, Becky! At least I’m not ________________.",
     "I lost my arm in a ________ accident.",
     "Isn’t this great, honey? Just you, me, the kids, and ____________.",
     "Foolish child! Did you think you could escape from ________________?",
     "Girls just wanna have ___________.",
     "Run, run, as fast as you can. You can’t catch me, I’m _____________!",
     "New from Mattel, it’s _______ Barbie!",
     "No fair! How come Chloe gets her own phone, and all I get is ________________?",
     "Bow before me, for I am the Queen of ______________!",
     "New from Hasbro! It’s BUNGO: The Game of ________.",
     "I don’t really know what my mom’s job is, but I think it has something to do with ____________.",
     "Our day at the water park was totally ruined by _____________.",
     "Charmander has evolved into ________________!",
     "What killed Old Jim?",
     "Next from J.K. Rowling: Harry Potter and the Chamber of ________________.",
     "What’s keeping Dad so busy in the garage?",
     "Boys? No. ____________? Yes!",
     "ME HUNGRY. ME WANT ______.",
     "Oh, that’s my mom’s friend Carl. He comes over and helps her with ____________.",
     "Guys, stop it! There’s nothing funny about ________________.",
     "Huddle up, Wildcats! They may be bigger. They may be faster. But we’ve got a secret weapon: ________________.",
     "Coming to theaters this holiday season, “Star Wars: The Rise of _________.”",
     "I do not fight for wealth. I do not fight for glory.",
     "I fight for _______!",
     "Come on, Danny. All the cool kids are doin’ it. Wanna try _____________?"]

# clears the window
def clearTerminal():
    print('\n'*100)


# creates the players
def createPlayers(num_players):
    players = []
    for i in range(0, num_players):
        print("What is the name of player " + str(i + 1))
        name = input()
        player = Player(name)
        players.append(player)
    return players


# lists the players
def printPlayers(players):
    print("PLAYERS:")
    for player in players:
        print(player)
    print('\n\n\n')


# checks to see if input is in range
def inputInRange(min_val, max_val):
    while True:
        user_input = input()
        if not user_input.isdigit():
            print("Sorry, that input is incorrect")
            continue
        elif int(user_input) not in range(min_val, max_val + 1):
            print("Sorry, that input is out of range")
            continue
        else:
            return int(user_input)


# check to see if input is out of range
def inputIsInt():
    while True:
        user_input = input()
        if not user_input.isdigit():
            print("Sorry, that input is incorrect")
            continue
        else:
            return int(user_input)

        # prompts the user to press enter


def pressEnter():
    print("Press the 'Enter' key to continue")
    input()


#sets up the game
def gameSetup_Mature(MatureWhiteCards, MatureBlackCards):
    clearTerminal()
    random.shuffle(MatureBlackCards)
    random.shuffle(MatureWhiteCards)
    print("""
    Welcome to Cards Against Humanity. This is a party game made for horrible people. 
    Give it a try and see if you're a horrible person. If you are, it's ok so are we.
    """"")
    pressEnter()

    #select the number of players
    print("How many people would you like to play? Minimum is 3, Maximum is 10")
    num_players = inputInRange(3,10)
    print(str(num_players) + " people are playing\n")

    #select how many points are needed
    print("How many points are needed to win?")
    max_points = inputIsInt()
    print("A player needs " + str(max_points) + " points to win\n")

    #name the players
    players = createPlayers(num_players)
    printPlayers(players)
    clearTerminal()
    return players, MatureWhiteCards, MatureBlackCards, max_points

#sets up the game
def gameSetup_Clean(MatureWhiteCards, CleanBlackCards):
    clearTerminal()
    random.shuffle(CleanBlackCards)
    random.shuffle(MatureWhiteCards)
    print("""
    Welcome to Kids Against Maturity. This is a party game where being the worst is the best!. 
    Give it a try and see if you're the worst. If you are, it's ok so are we.
    """"")
    pressEnter()

    #select the number of players
    print("How many people would you like to play? Minimum is 3, Maximum is 10")
    num_players = inputInRange(3,10)
    print(str(num_players) + " people are playing\n")

    #select how many points are needed
    print("How many points are needed to win?")
    max_points = inputIsInt()
    print("A player needs " + str(max_points) + " points to win\n")

    #name the players
    players = createPlayers(num_players)
    printPlayers(players)
    clearTerminal()
    return players, whiteCards, blackCards, max_points

# this object represents a player
class Player(object):
    def __init__(self, name):
        # instance variables
        self.name = name
        self.black_deck = []
        self.white_deck = []
        self.points = 0

    # toString method of user
    def __str__(self):
        return self.name

    # gets the specific card from user's deck
    def pickCard(self, card_index):
        return white_deck[card_index]

    # adds a response card to user's deck
    def addResponseCard(self, response_card):
        self.white_deck.append(response_card)

    # adds a prompt card to user's deck
    def addPromptCard(self, prompt_card):
        self.black_deck.append(prompt_card)

    # adds a list of response cards to user's deck
    def addMultipleCards(self, cards):
        for card in cards:
            self.addResponseCard(card)

    # removes a response card from user's deck
    def removeResponseCard(self, card_index):
        return self.white_deck.pop(card_index)

    # adds a point to the user
    def addPoint(self):
        self.points += 1

    # gets the user's name
    def getName(self):
        return self.name

    # gets the user's score
    def getScore(self):
        return self.points

    # get's the user's prompt deck
    def getPromptDeck(self):
        return self.black_deck

    # get's the user's response deck
    def getResponseDeck(self):
        return self.white_deck


# This is the game board
class Game(object):
    def __init__(self, players, response_cards, prompt_cards, max_points):
        # instance variables
        self.players = players
        self.response_cards = response_cards
        self.prompt_cards = prompt_cards
        self.max_points = max_points
        self.used_prompt_cards = []
        self.used_response_cards = []
        self.current_prompt_card = None
        self.card_czar = None
        self.card_czar_index = 0

    # method which starts and runs the game
    def start(self):
        self.handOutCards()
        # keep gaming continuing until winner
        while not self.isWinner():
            self.displayScore()
            self.rotateCardCzar()
            self.selectPromptCard()
            responses = self.getPlayerResponseCards()
            self.chooseWinningCard(responses)
        self.winningMessage(self.isWinner())

    # hand out starter cards to players
    def handOutCards(self):
        for player in self.players:
            player.addMultipleCards(self.response_cards[:7])
            self.response_cards = self.response_cards[7:]

    # rotate card czar every round
    def rotateCardCzar(self):
        new_czar_index = self.card_czar_index % len(self.players)
        self.card_czar = self.players[new_czar_index]
        self.card_czar_index += 1
        print("CARD CZAR ROTATION: " + self.card_czar.getName() + " is now the Card Czar\n")

    # returns the winner if they achieve points needed
    def isWinner(self):
        for player in self.players:
            if player.getScore() == self.max_points:
                return player
        return ""

    # selects the prompt card for the round
    def selectPromptCard(self):
        self.current_prompt_card = self.prompt_cards.pop(0)
        print(self.card_czar.getName() + " selected the prompt card\n")
        self.displayPromptCard()
        pressEnter()

    # prints prompt card
    def displayPromptCard(self):
        print("PROMPT:")
        print(self.current_prompt_card + "\n")

    # rotate through players and get their responses to prompt
    def getPlayerResponseCards(self):
        playerResponses = []
        for i in range(0, len(self.players) - 1):
            # get next player
            player = self.rotatePlayer(i)
            clearTerminal()
            print(player.getName() + "'s response selection is next")
            pressEnter()
            print(player.getName() + "'s Response Selection\n")
            self.displayPromptCard()
            player_deck = player.getResponseDeck()
            # ask player for their response
            self.printPlayerResponseDeck(player_deck)
            card_index = self.askPlayerInput(player_deck)
            player_card = player_deck[card_index]
            print("You've selected " + player_card + "\n")
            playerResponses.append({'player': player, 'response': player_card})
            # player picks up a new card from the response deck
            self.pickUpNewCard(player, card_index)
            pressEnter()
        clearTerminal()
        print(self.card_czar.getName() + ", the Card Czar will now choose his favorite card")
        pressEnter()
        return playerResponses

    # selects the next player for their responses
    def rotatePlayer(self, index):
        new_player_index = (self.card_czar_index + index) % len(self.players)
        return self.players[new_player_index]

    # prints a players response deck
    def printPlayerResponseDeck(self, player_deck):
        print("The option's\n")
        for index, card in enumerate(player_deck):
            print(str(index) + ": " + card + "")
        print("\n")

    # ask a player for their input to a question
    def askPlayerInput(self, player_deck):
        print("Which card do you want to select? Enter the card's number")
        user_val = inputInRange(0, len(player_deck) - 1)
        return int(user_val)

    # player picks up a new card
    def pickUpNewCard(self, player, card_index):
        used_card = player.removeResponseCard(card_index)
        self.used_response_cards.append(used_card)
        player.addResponseCard(self.response_cards.pop(0))

    # card czar chooses his favorite card
    def chooseWinningCard(self, responses):
        print("CARD CZAR SELECTION\n")
        print(self.card_czar.getName() + ", please select your favorite card\n")
        self.displayPromptCard()
        listOfResponses = [d['response'] for d in responses]
        self.printPlayerResponseDeck(listOfResponses)
        user_val = self.askPlayerInput(listOfResponses)
        winning_card = listOfResponses[user_val]
        winner = responses[user_val]['player']
        print("The winning card is " + winning_card + "\n")
        print(winner.getName() + " won this round!\n")
        winner.addPromptCard(self.current_prompt_card)
        self.updateScore(winner)
        pressEnter()
        clearTerminal()

    # updates the scoreboard
    def updateScore(self, winner):
        winner.addPoint()

    # displays the scoreboard
    def displayScore(self):
        print("\n\nSCOREBOARD")
        for player in self.players:
            print("Player: " + player.getName() + "\tScore: " + str(player.getScore()))
        print("\n")

    # displays the winner and their won cards
    def winningMessage(self, winner):
        self.displayScore()
        print(winner.getName() + " is the winner!\n")
        print(winner.getName() + " won the cards: ")
        for card in winner.getPromptDeck():
            print(card)

def pick():
    Mode = int(input("Before we begin, what is the age of the youngest player? "))
    if Mode <= 17:
        # set up the game
        players, blackCards_shuffled, whiteCards_shuffled, max_points = gameSetup_Clean(CleanWhiteCards,
                                                                                         CleanBlackCards)
        # start the game
        game = Game(players, blackCards_shuffled, whiteCards_shuffled, max_points)
        game.start()

    elif Mode >= 18:
        #set up the game
        players, blackCards_shuffled, whiteCards_shuffled, max_points = gameSetup_Mature(MatureWhiteCards,
                                                                                         MatureBlackCards)
        #start the game
        game = Game(players, blackCards_shuffled, whiteCards_shuffled, max_points)
        game.start()

pick()