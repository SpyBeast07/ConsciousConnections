label start:

play music "audio/mooosic.mp3"

define teacher = Character('Teacher', color="#1e00ff")
define child = Character('Child', color="#1e00ff")
define girl = Character('Girl', color="#1e00ff")
define boy = Character('Boy', color="#1e00ff")
define friend = Character('Friend', color="#1e00ff")
define mother = Character('Mother', color="#1e00ff")
define dad = Character('Dad', color="#1e00ff")
define emily = Character('Emily', color="#1e00ff")
define alex = Character('Alex', color="#1e00ff")
define jake = Character('Jack', color="#1e00ff")
define brother = Character('Brother', color="#1e00ff")
define michael = Character('Michael', color="#1e00ff")
define alice = Character('Alice', color="#1e00ff")
define henry = Character('Henry', color="#1e00ff")
define vihan = Character('Vihan', color="#1e00ff")
define lily = Character('Lily', color="#1e00ff")
define emma = Character('Emma', color="#1e00ff")
define doctor = Character('Doctor', color="#1e00ff")

label gender:

    menu:
        "Choose your gender"
        "Boy":
            $ child = boy
        "Girl":
            $ child = girl

label Kitchen:
    image img1 = "images/Kitchen.png"
    show img1

    
    child "(approaching her mother) Mom, I'm experiencing some changes in my body and I don't know why they're happening."
    

    
    mother "What kind of changes, dear?"

    if child == boy:
        
        child "Like hair growth in new places, and I feel emotions changing quickly - happy, sad, and angry. I feel uncomfortable and a fluid is coming out."
    else:
        
        child "Like hair growth in new places, and I feel emotions changing quickly - happy, sad, and angry. I also feel a heaviness in my chest and some white fluid coming out of my body."

    mother "Oh, don't worry, it's natural. These changes happen to everyone."

    
    child "But Mom, why do they happen?"

    mother "I'm busy right now, dear. Don't bother me. This is something you will know as you will grow up."

    hide img1


label LivingRoom:
    image img2 = "images/LivingRoom.png"
    show img2 at center:
        xzoom 0.6
        yzoom 0.6

    "The Child then goes to her father for help."

    
    child "Dad, can you help me? I'm having some issues."

    
    dad "What kind of issues?"

    if child == boy:
        
        child "Like hair growth in new places, and I feel emotions changing quickly - happy, sad, and angry. I feel uncomfortable and a fluid is coming out."
    else:
        
        child "Like hair growth in new places, and I feel emotions changing quickly - happy, sad, and angry. I also feel a heaviness in my chest and some white fluid coming out of my body."

    
    dad "(feeling awkward and avoiding eye contact) I'm not sure about that. Ask your mother."

    
    child "I already did, but she didn't answer."

    
    dad "In that case, you can ask your teacher. I have a lot of work to do right now, so please don't disturb me."

    hide img2


image img3 = "images/Room.png"
show img3 at center:
    xzoom 1.95
    yzoom 1.95


"The child then quietly sits aside, feeling confused and frustrated."

"The next day in school...
IN CLASSROOM - DAY"

hide img3

label classroom:
    image img4 = "images/ClassRoom.png"
    show img4

    "A biology teacher is standing in front of a class full of students. The topic is reproduction, and the teacher is explaining the process of fertilization."

    
    teacher "So, the sperm and the egg combine to form a zygote, which will eventually develop into a fetus."

    "Suddenly, a child in the front row raises their hand."

    
    teacher "Yes, what is it?"

    
    child "I'm having difficulty understanding how the sperm and the egg find each other. Could you please explain it again?"

    "The teacher appears to be a bit taken aback."

    
    teacher "(awkwardly) Well, that's a rather personal question."

    
    child "I'm sorry, I just really want to understand this concept better."

    
    teacher "(giggling nervously) I understand, but that's not really something we can discuss in class."

    
    child "I'm not trying to be inappropriate, I just want to learn."

    
    teacher "(pausing) I appreciate your curiosity, but we may need to discuss this topic at a more appropriate time. Let's focus on the material for today."

    "The teacher then continues with the lesson, hoping to avoid further discussion on the matter."

    hide img4


label playground:
    image img5 = "images/Field.png"
    show img5

    "In playground"

    
    child "(talking to his friend) I don't understand why nobody wants to answer my queries. It's like they're all avoiding the topic."

    
    friend "(listening intently) Yeah, I know what you mean. It can be really confusing and frustrating."

    
    child "(sighing) I just wish there was someone who could help me understand it better."

    
    friend "Actually, my sister told me about this stuff. She said that a lot of people think it's taboo to talk about, but it's really important to understand."

    
    child "(perking up) Really? What did she tell you?"

    
    friend "Well, she gave me some basic information, but then she also introduced me to this cool game that helped me learn more about it."

    
    child "(curiously) A game? What kind of game?"

    
    friend "It's a sex education game that covers all the basics, but it's designed to be fun and engaging. You can learn a lot from playing it."

    
    child "(intrigued) That sounds like it could be really helpful. Can you tell me more about it?"

    
    friend "Sure, I will send you the link of the game, when I reach home."

    
    child "Cool!!"

    "Now he went to home and played the game."

    hide img5


image img = "images/room_dusk_light_on.png"
show img

label BrotherTalks:
    "Game Starts"
    menu:
        "Choose your gender"
        "Boy":
            $ child = boy
        "Girl":
            $ child = girl
    
    
    child "(whispers) Hey, have you heard about puberty and stuff?"
    

    
    brother "Yeah, I have. Why do you ask?"
    

    
    child "I'm just really confused about it all. Like, what happens to our bodies during puberty and how do we deal with it? We had a discussion in class over this but our teacher was not very clear can you help me understand all these terms."
    

    
    brother "Well, puberty is a time when our bodies go through a lot of changes. It's perfectly normal to feel confused or uncomfortable about it, but it's important to understand what's happening."
    

    
    child "Can you explain more about the changes that happen in our bodies?"
    

    
    brother "Sure, during puberty, your body starts producing hormones that cause changes like breast development, body hair growth, and menstruation in girls. Boys also go through changes like voice deepening, muscle growth, and facial hair growth."
    

    
    child "Oh, I see. What about periods and stuff? I don't know anything about that."
    
    
    
    brother "That's completely understandable. Periods are a natural part of a girl's life and happen once a month. It's important to have good hygiene during that time and to use pads or tampons to manage the bleeding."
    

    
    child "What if I don't have access to pads or tampons?"
    

    
    brother "It's important to talk to a trusted adult, like a parent or teacher, and ask for help. They can provide you with the necessary supplies or help you find resources to get them."
    

    
    child "(looks worried)My friend was crying today saying that he don’t like his uncle at all because he touches him in a very unadequate manner and he don’t like it at all and teacher said he is facing sexual abuse by his uncle. So I want to ask What is sexual abuse?"
    

    
    brother "Unfortunately, that's true. It's important to know that no one has the right to touch you inappropriately, and if that ever happens, you need to tell someone you trust, like a parent or teacher. It's also important to know that it's never your fault and there are people who can help you."
    

    
    child "What should I do if I witness someone else being sexually abused?"
    

    
    brother "It's important to tell a trusted adult or call the police immediately. You can also speak to a counselor or social worker for support."
    

    
    child "(nods) Okay, thanks for explaining all of this to me. I feel a lot better now."
    


    brother "No problem. It's important to be informed about these things, so you can take care of yourself and stay safe. And remember, if you ever have any questions or concerns, don't be afraid to ask for help."
    

hide img

image imge = "images/room_evening_light_off.png"
show imge

label emily:
    "Level 2 - Learning basics about sexual education"
    if child == boy:
        "Michael turned 13 year old and was enjoying his school, but he suddenly felt very different in his body and was confused but carried the confusion as there was no clear guidance. With time she grew many different habits and turned into a new person. Some of the habits were not good enough and he was not happy with those like Michael  had a habit of watching porn that he couldn't seem to shake. He felt lonely and bored and turned to it for excitement. Despite her best efforts, he couldn't overcome the addiction."
        "One day, he fell in love with a girl at school and approached her. They hit it off and soon found themselves in a happy relationship."
        "However, after a year together, Michael started to notice that Alice and Sarah were spending a lot of time together. He felt uneasy and confronted Alice about it."
        
        
        michael "Why do you spend so much time with Sam? Don't you care about our relationship?"
        

        
        alice "Of course, I care about our relationship. Sam and I are just friends, there's nothing going on between us."
        

        
        michael "I don't believe you. You're always with her and you never seem to have time for me anymore."
        

        
        alice "That's not true. I've been busy with school lately, but I still love you and want to make things work."
        

        
        michael "I just don't know if I can trust you anymore."
        
        "Michael leaves. Alice tried to reach out to Michael several times, but he wouldn't respond. She sent him messages and tried calling him, but he remained distant and unresponsive."
        "After few weeks,
        Michael was sitting and chilling with his friend Max. He felt uneasy but talked to Max."

        
        michael "(sighs) I can't believe I'm watching porn. It's not who I am."
        

        
        henry "What's going on?"
        

        
        michael "I feel so bored and lonely lately, I guess I turned to it for some excitement."
        

        
        henry "Have you talked to anyone about it?"
        

        
        michael "No, I don't want people to think I'm weird or anything."
        

        
        henry "It's completely normal to feel that way sometimes. But watching porn won't solve the problem. Maybe you should consider talking to someone, like our school counselor. Sex is about mutual pleasure and communication. You should be able to talk about it freely."
        

        
        michael "(nods) You're right, thanks for being there for me."
        

        
        henry "Of course, but there's something else I want to talk to you about. Alice."
        

        
        michael "(angrily) I don't want to talk about her at all!"
        

        
        henry "I know you're upset, but have you given her a chance to explain herself?"
        

        
        michael "What's there to explain? She cheated on me with that Sarah!"
        

        
        henry "No, she didn't. They're just good friends, trust me. At least talk to her once and hear her out."
        

        
        michael "(skeptical) I don't know..."
        

        
        henry "Please, trust me. You won't regret it."
        
        
        image imgx = "images/uncle mugen school corridor morning.png"
        show imgx

        menu:
            "Should you talk to her or not"
            "(reluctantly) Fine. I'll talk to her, but only for five minutes.":
                "Michael talked to Alice next day in school"

                
                michael "Hello, Alice. You have five minutes to explain everything."
                

                
                alice "Thank you for giving me the chance to talk to you. I just want to say that I never cheated on you with Sarah. She's just a friend."
                

                
                michael "(doubtful) But I saw you two together all the time!"
                

                
                alice "I know, but that's because we were working on a project together. I swear, there was nothing going on between us."
                

                
                michael "(pauses) Okay, I'll believe you. I'm sorry for not listening to you earlier."
                

                
                alice "It's okay, I understand why you were upset. But we need to communicate better in our relationship. We can't let our insecurities and misunderstandings get in the way."
                

                
                michael "(smiling) You're right. I'm glad we talked this out."
                

                image imgy = "images/seaside_road_morning.png"
                show imgy

                "Michael and Alice were able to sort out their differences and return to a happy relationship. They communicated more openly and worked on their insecurities together. However, after a year, they went their separate ways due to college and other priorities. They remained on good terms and wished each other the best in their futures."

            
            "No, I don’t want to talk about it at all.":
                image imgy = "images/seaside_road_morning.png"
                show imgy
                
                "Michael and Alice were not able to sort out their differences and return to a happy relationship because they never communicated openly and never worked on their insecurities together. After a year they went their separate ways due to college and other priorities."
            
        hide imgx
        hide imgy

    else:
        image imgk = "images/room_evening_light_off.png"
        show imgk

        "Emily turned 13 year old and was enjoying her school, but she suddenly felt very different in her body and was confused but carried the confusion as there was no clear guidance. With time she grew many different habits and turned into a new person. Some of the habits were not good enough and she was not happy with those like Emily had a habit of watching porn that she couldn't seem to shake. She felt lonely and bored and turned to it for excitement. Despite her best efforts, she couldn't overcome the addiction. "
        "One day, she fell in love with a boy at school and approached him. They hit it off and soon found themselves in a happy relationship."
        "However, after a year together, Emily started to notice that Alex and Sarah were spending a lot of time together. She felt uneasy and confronted Alex about it."
        
        
        emily "Why do you spend so much time with Sarah? Don't you care about our relationship?"
        

        
        alex "Of course, I care about our relationship. Sarah and I are just friends, there's nothing going on between us."
        

        
        emily "I don't believe you. You're always with her and you never seem to have time for me anymore."
        

        
        alex "That's not true. I've been busy with school lately, but I still love you and want to make things work."
        

        
        emily "I just don't know if I can trust you anymore."
        
        
        "Emily leaves. Alex tried to reach out to Emily several times, but she wouldn't respond. He sent her messages and tried calling her, but she remained distant and unresponsive. "
        "After few weeks,
        Emiliy was sitting and chilling with her friend Mia. She felt uneasy but talked to Mia "

hide imge
hide imgx
hide imgk

image imgg = "images/room_evening_light_off.png"
show imgg

label TeraSatara:
    if child == girl:
        $ girl = emily
        girl "sighs I can't believe I'm watching porn. It's not who I am."
        

        
        friend "What's going on?"
        

        
        girl "I feel so bored and lonely lately, I guess I turned to it for some excitement."
        

        
        friend "Have you talked to anyone about it?"
        

        
        girl "No, I don't want people to think I'm weird or anything."
        

        
        friend "It's completely normal to feel that way sometimes. But watching porn won't solve the problem. Maybe you should consider talking to someone, like our school counselor. Sex is about mutual pleasure and communication. You should be able to talk about it freely."
        

        
        girl "(nods) You're right, thanks for being there for me."
        

        
        friend "Of course, but there's something else I want to talk to you about. Alex."
        

        
        girl "angrily I don't want to talk about him at all!"
        

        
        friend "I know you're upset, but have you given him a chance to explain himself?"
        

        
        girl "What's there to explain? He cheated on me with that Sarah!"
        

        
        friend "No, he didn't. They're just good friends, trust me. least talk to him once and hear him out."
        

        
        girl "(skeptical) I don't know...."
        

        
        friend "Please, trust me. You won't regret it."
        

        menu:
            "Do you want to talk to Alex?"
            "Reluctantly Fine. I'll talk to him, but only for five minutes.":
                "Emily talk to Alex next day in school "

                
                girl "Hello, Alex. You have five minutes to explain everything."
                

                
                alex "Thank you for giving me the chance to talk to you. I just want to say that I never cheated on you with Sarah. She's just a friend."
                

                
                girl "doubtful But I saw you two together all the time!"
                

                
                alex " I know, but that's because we were working on a project together. I swear, there was nothing going on between us."
                

                
                girl "(pauses) Okay, I'll believe you. I'm sorry for not listening to you earlier. "
                
                
                
                alex "It's okay, I understand why you were upset. But we need to communicate better in our relationship. We can't let our insecurities and misunderstandings get in the way."
                

                
                girl "(smiling) You're right. I'm glad we talked this out."
                

                image imagh = "images/seaside_road_morning.png"
                show imagh
                "Emily and Alex were able to sort out their differences and return to a happy relationship. They communicated more openly and worked on their insecurities together. However, after a year, they went their separate ways due to college and other priorities. They remained on good terms and wished each other the best in their futures. "
            
            "No, I don’t want to talk about it at all.":
                image imagh = "images/seaside_road_morning.png"
                show imagh
                "Emily and Alex were not able to sort out their differences and return to a happy relationship because they never communicated openly and never worked on their insecurities together. After a year they went their separate ways due to college and other priorities. They remained on good terms and wished each other the best in their futures. "
hide imagg
hide imagh

image imgo = "images/library.png"
show imgo at center:
    xzoom 1.6
    yzoom 1.6
    

label AtharaPalas:
    "Level 3"
    if child == girl:
        "Emily reached at the age of 18 and started to go college."
        "COLLEGE CAMPUS - DAY"

        menu:
            "Choose whom to date....."
            "Jake":
                "Emily is walking around the campus, looking at all the different buildings. She bumps into a tall, handsome guy named Jake."

                
                jake "(smiling) Hey there! I'm Jake. What's your name?"
                

                
                emily "(smiling) Hi, Jake. I'm Emily."
                

                
                jake "(smiling) It's nice to meet you, Emily."
                

                hide imgo
                image imgp = "images/anime-original-cafe-wallpaper-preview.png"
                show imgp:
                    xzoom 2.65
                    yzoom 2.65

                "CUT TO: INT. COFFEE SHOP DAY(goes on dates)"

                "Emily and Jake are sitting across from each other, drinking coffee and talking."
                
                
                emily "(smiling) So, what do you like to do for fun?"
                

                
                jake "(smiling) Oh, I like to play basketball, hang out with friends, and go to parties."
                

                
                emily "(smiling) That sounds like fun."
                
                            
                menu:
                    "Consent not taken":
                        hide imgp
                        image imgq = "images/08372db177b3bde1453c5a8a8ccbddf1.png"
                        show imgq
                        "CUT TO: INT. PARTY HOUSE - NIGHT"
                        "Emily and Jake are at a party, dancing and having fun. They go into a room, and Jake starts to touch Emily all over her body. Emily tries to push him away and tells him to stop, but he doesn't listen. Jake pushes Emily onto the bed and forces himself on her. Emily is traumatized and feels violated.  "
                        
                        hide ingq
                        image imgr = "images/desktop-wallpaper-anime-bedroom-background-day-di-2020-ide-kamar-tidur-desain.png"
                        show imgr
                        
                        "CUT TO: INT. EMILY'S ROOM - DAY"
                        "Emily is sitting on her bed, crying. Her friend comes in and sees her crying."

                        
                        friend "(concerned) Emily, what's wrong?"
                        

                        
                        emily "(crying) Jake violated me at the party. I feel so insecure and not good."
                        

                        
                        friend "(supportive) I'm so sorry that happened to you. You didn't deserve that. You should report it and should get justice."
                        

                        menu:
                            "Reports him:":
                                hide imgr
                                image imgs = "images/86eea9465e29bba0a2f3f35cca618ad2cd828c49_2_690x407.png"
                                show imgs at center:
                                    xzoom 2.7
                                    yzoom 2.7
                                "CUT TO: INT. CAMPUS SECURITY OFFICE - DAY"

                                "Emily is sitting in front of the campus security officer, reporting Jake's violation."

                                
                                emily "(determined) I want to report Jake's violation. He needs to be held accountable for his actions."
                                

                                "Later, news circulates in college that Jake gets relitigated."

                                "CUT TO: INT. EMILY'S ROOM - DAY"

                                " Emily's friend is sitting next to her, trying to cheer her up."

                                
                                friend "(supportive) You did the right thing by reporting Jake. You have nothing to feel guilty about."
                                

                                
                                emily "(smiling) Thank you. I'm just glad that justice was served."
                                
                            
                            "Doesn't Report:":
                                "Emily does not report him. Jake continues to harass her without consent. They have a toxic relationship and it continues as she doesn’t take any strict actions against it. It affects her mental health as well as increases depression. "
                    
                    "Consent taken":
                        hide imgp
                        image imgq = "images/08372db177b3bde1453c5a8a8ccbddf1.png"
                        show imgq

                        
                        jake "I really like you, Emily. Do you want to take things to the next level?"
                        

                        
                        emily "(looking nervous but interested) Yes, I do."
                        

                        "Jake and Emily start making out, and eventually Jake tries to touch her all over her body after taking her consent."
                        
                        hide imgq
                        image imgr = "images/11636386596ectvdfgg626gwvk2qewkwxiiutprfsukyrdxwp0trkb0hd8do7auzvb95fc4zg4yilwkftnlshhnsbo3bo3vaz4nvujxtmsapisq.png"
                        show imgr

                        "INT. EMILY'S DORM ROOM - DAY"

                        "Emily wakes up the next morning feeling confused and guilty. She realizes that they didn't use any contraception and is worried she might be pregnant."

                        
                        emily "(talking to herself) Oh my god, what have I done? What if I'm pregnant?"
                        

                        "Emily takes a pregnancy test and confirms her worst fears. She's pregnant."

                        
                        emily "(crying) How am I going to tell Jake?"
                        

                        "INT. JAKE'S DORM ROOM - DAY"
                        "Emily tells Jake the news, and he's shocked and confused."

                        menu:
                            "Do Jake...."
                            "doesn't takes responsibility":
                                
                                jake "(stumbling over his words) I didn't think this would happen. I'm not ready to be a dad."
                                

                                
                                emily "(crying) I understand, but I can't do this alone."
                                

                                
                                jake "(sighing) I'm sorry, Emily. I can't take responsibility for this."
                                

                                "INT. EMILY'S DORM ROOM - DAY"

                                "Emily is alone, crying, and feeling scared about the future. She realizes that she has to take responsibility for her child and raise him/her on her own."

                                
                                emily "(talking to herself) I can do this. I have to be strong for my baby."
                                

                                "INT. EMILY'S APARTMENT - DAY"
                                "Emily is holding her newborn baby, looking happy and content."
                                
                                
                                emily "(to her baby) I'll always love you and take care of you, no matter what."
                                
                                
                            "takes responsibility":
                                
                                jake "(stumbles) I...I don't know what to say."
                                

                                
                                emily "(tearfully) I understand if you don't want to be involved, but I'm keeping the baby."
                                

                                
                                jake "(sighs) No, Emily. I'll take responsibility for our child. We'll figure this out together."
                                

                                "Emily and Jake hug, and Emily feels relieved that Jake is willing to support her."

            "Vihan":
                "Emily, a bright-eyed and eager 18-year-old girl, walks around the college campus, excited to start her new journey. She spots a tall, handsome guy named Vihaan, who catches her attention. Vihaan is a friendly and kind person who is loved by everyone. "

                
                emily "(to herself) Wow, who is that guy? He seems so calm and collected."
                

                "Emily goes about her day, but she keeps running into Vihaan. They have a few brief conversations, and Emily finds herself drawn to him. She can't stop thinking about him."

                "A few days later, Emily is running late for class and accidentally bumps into Vihaan, causing her to fall to the ground. Vihaan quickly offers his hand to help her up, and they exchange a few words before going their separate ways. Emily is happy to have interacted with Vihaan and starts having feelings for him."

                "Days pass, and Emily and Vihaan start seeing each other more often. They hang out together, and Emily falls deeply in love with him. One night, they take their relationship to the next level and have their first sexual experience together."

                
                emily "(whispering) Vihaan, are you sure you want to do this?"
                

                
                vihan "(smiling) Yes, I'm sure."

                menu:
                    "Emily and Vihaan have decided to take their relationship to the next level and have their first sexual experience together. However, during their intimacy, Vihaan struggles to get excited and becomes depressed."
                    "Does not explain the situation":
                        "Emily is confused and insecure, thinking that Vihaan isn't feeling the same way she is."

                        
                        vihan "(muttering to himself) Why is this happening? I can't get excited."
                        

                        "Vihaan doesn't explain the situation to Emily, as he is embarrassed about what has happened."
                        "The next day, Emily tries to talk to Vihaan about it, but he ignores her, saying he has class and isn't free all day. The communication gap widens between them, leading to their eventual breakup, and they go their separate ways."

                        
                        emily "(voice trembling) Vihaan, please talk to me. What's going on?"
                        

                        
                        vihan "(coldly) I can't talk right now. I have to go to class."
                        

                        "Emily is heartbroken and can't believe what has just happened. She walks away with tears in her eyes."

                        
                        emily "(voice cracking) Why won't he talk to me? What did I do wrong?"
                        

                        "As Emily walks away, she realizes that love can be painful and confusing, but she is determined to move forward and find happiness."

                    "Explains the situation":
                        "Emily becomes confused and concerned, so she asks Vihaan what's going on."
                        "Vihaan feels embarrassed but tries to explain the situation to her."

                        
                        vihan "I'm sorry, Emily. I'm just not feeling it. I don't know what's wrong with me."
                        

                        "Emily is understanding and supportive, but she doesn't have much knowledge about it, so they decide to research the issue."
                        
                        image imgn = "images/11636386596ectvdfgg626gwvk2qewkwxiiutprfsukyrdxwp0trkb0hd8do7auzvb95fc4zg4yilwkftnlshhnsbo3bo3vaz4nvujxtmsapisq.png"
                        show imgn

                        "INT. EMILY'S ROOM - DAY"
                        "Emily and Vihaan are researching sexual dysfunction on Emily's laptop. They also reach out to their parents and friends for advice."

                        hide imgn
                        image imgo = "images/Clinic.png"
                        show imgo

                        "INT. DOCTOR’S OFFICE - DAY"
                        "Emily and Vihaan visit a doctor who explains the situation to them. The doctor tells them that sexual dysfunction is quite common and normal among young people and suggests some prescriptions for Vihaan."
                        "The doctor also advises them to be patient and communicate with each other. He reassures them that this is a treatable condition and there is nothing to be ashamed of."

                        hide imgo
                        image imgn = "images/VihanR.png"
                        show imgn

                        "INT. VIHAAN’S DORM ROOM - NIGHT"
                        "Vihaan takes the prescribed medication and he and Emily try again. This time, it is a success, and they both feel happy and satisfied."

                        hide imgn
                        image imgt = "images/11636386596ectvdfgg626gwvk2qewkwxiiutprfsukyrdxwp0trkb0hd8do7auzvb95fc4zg4yilwkftnlshhnsbo3bo3vaz4nvujxtmsapisq.png"
                        show imgt

                        "INT. EMILY'S ROOM - DAY"
                        "Emily and Vihaan discuss their journey and how they overcame the problem together. They realize that communication and understanding are key to a healthy relationship."
                        
                        hide imgt
                        image imgu = "images/VihanR.png"
                        show imgu

                        "INT. VIHAAN’S DORM ROOM - DAY"
                        "Vihaan tells Emily that he loves her and wants to spend the rest of his life with her. Emily reciprocates his feelings and they decide to take their relationship to the next level and have a happy family."
    else:
        "Michael reached at the age of 18 and started to go college."
        "COLLEGE CAMPUS - DAY"

        menu:
            "Choose whom to date....."
            "Lily":
                "Michael is walking around the campus, looking at all the different buildings. He bumps into a beautiful girl named Lily. "

                
                lily "(smiling) Hey there! I'm Lily. What's your name?"
                

                
                michael "(smiling) Hi, Lily. I'm Michael."
                

                
                lily "(smiling) It's nice to meet you, Michael."
                

                hide imgo
                image imgp = "images/anime-original-cafe-wallpaper-preview.png"
                show imgp:
                    xzoom 2.65
                    yzoom 2.65

                "CUT TO: INT. COFFEE SHOP DAY(goes on dates)"

                "Michael and Lily are sitting across from each other, drinking coffee and talking."
                
                
                michael "(smiling) So, what do you like to do for fun?"
                

                
                lily "(smiling) Oh, I like to paint, read books, and go to the beach."
                

                
                michael "(smiling) That sounds like fun."
                
                            
                menu:
                    "Consent not taken":
                        hide imgp
                        image imgq = "images/08372db177b3bde1453c5a8a8ccbddf1.png"
                        show imgq
                        "CUT TO: INT. PARTY HOUSE - NIGHT"
                        "Michael and Lily are at a party, dancing and having fun. They go into a room, and Lily starts to touch James all over his body. James tells her to stop, but she doesn't listen. Lily pushes James onto the bed and tries to force herself on him. James manages to push her off and gets out of the room. He feels traumatized and violated."
                        
                        hide ingq
                        image imgr = "images/desktop-wallpaper-anime-bedroom-background-day-di-2020-ide-kamar-tidur-desain.png"
                        show imgr
                        
                        "CUT TO: INT. Michael'S ROOM - DAY"
                        "Michael is sitting on his bed, feeling distressed. His friend comes in and sees him upset."

                        
                        friend "(concerned) Michael, what's wrong?"
                        

                        
                        michael "(upset) Lily tried to force herself on me at the party. I feel so violated and confused."
                        

                        
                        friend "(supportive) I'm so sorry that happened to you. You didn't deserve that. You should report it and should get justice."
                        


                        michael "(nodding) Yeah, you're right. I should report it."

                        menu:
                            "Reports her:":
                                hide imgr
                                image imgs = "images/86eea9465e29bba0a2f3f35cca618ad2cd828c49_2_690x407.png"
                                show imgs at center:
                                    xzoom 2.7
                                    yzoom 2.7
                                "CUT TO: INT. CAMPUS SECURITY OFFICE - DAY"

                                "Michael is sitting in front of the campus security officer, reporting Lily's violation."

                                
                                michael "(determined) I want to report Lily'sattempt to assault me. She needs to be held accountable for her actions. Later, news circulates in college that Sarah gets prosecuted."
                                

                                "Later, news circulates in college that Lily gets relitigated."

                                "CUT TO: INT. Michael'S ROOM - DAY"

                                "Michael's friend is sitting next to him, trying to cheer him up."

                                
                                friend "(supportive) You did the right thing by reporting lily. You have nothing to feel guilty about."
                                

                                
                                michael "(smiling) Thank you. I'm just glad that justice was served."
                                
                            
                            "Doesn't Report:":
                                "Michael does not report him. Lily continues to harass her without consent. They have a toxic relationship and it continues as she doesn’t take any strict actions against it. It affects her mental health as well as increases depression. "
                    
                    "Consent taken":
                        hide imgp
                        image imgq = "images/08372db177b3bde1453c5a8a8ccbddf1.png"
                        show imgq

                        
                        lily "I really like you, Michael. Do you want to take things to the next level?"
                        

                        
                        michael "(looking nervous but interested) Yes, I do."
                        

                        
                        hide imgq
                        image imgr = "images/11636386596ectvdfgg626gwvk2qewkwxiiutprfsukyrdxwp0trkb0hd8do7auzvb95fc4zg4yilwkftnlshhnsbo3bo3vaz4nvujxtmsapisq.png"
                        show imgr

                        "INT. Michael'S DORM ROOM - DAY"

                        "Michael wakes up the next morning feeling confused and guilty. He realizes that they didn't use any contraception and is worried he might have gotten Emma pregnant."

                        
                        michael "(talking to herself) Oh my god, what have I done? What if Lily is pregnant?"
                        

                        "Michael and Lily discuss the situation, and Lily takes a pregnancy test, confirming Michael's worst fears."

                        
                        lily "(crying) How are we going to handle this?"
                        


                        menu:
                            "Michael"
                            "Doesn't take responsibility":
                                "Michael tells lily that he is not ready to be a father and does not want to take responsibility for the pregnancy."

                                michael "(stumbling over his words) I didn't think this would happen. I'm not ready for this."
                                

                                
                                lily "(crying) I understand, but I can't do this alone."
                                
                                "Jake leaves lily alone to deal with the situation. lily is left feeling scared and uncertain about the future."
                                                                

                                "INT. lily'S DORM ROOM - DAY"

                                "lily is alone, crying, and feeling scared about the future. She realizes that she has to take responsibility for her child and raise him/her on her own."
                                

                                "INT. michael'S APARTMENT - DAY"
                                "lily is holding her newborn baby, looking happy and content."
                                
                                
                                michael "(to her baby) I'll always love you and take care of you, no matter what."
                                
                                
                            "take responsibility":

                                image imgm = "images/Hospital.png"
                                show imgm:
                                    xzoom 2.2
                                    yzoom 2.2

                                "INT. DOCTOR'S OFFICE - MONTHS LATER "

                                "lily and Michael are in the doctor's office, holding hands and looking at the ultrasound of their baby."
                                
                                lily "(stumbles) I...I don't know what to say."
                                
                                doctor "Congratulations, it's a girl!"
                                
                                michael "(smiling) That's great news."

                                "INT. lily AND MICHAEL'S APARTMENT - DAY"

                                "lily and Michael are setting up the nursery for their baby girl."

                                michael "(excitedly) I can't wait to teach her how to play basketball."

                                lily "(laughing) And I'll teach her how to paint."
                                
                                michael "(smiling) We'll give her the best of both worlds."

                                "INT. HOSPITAL ROOM - DAY"

                                "lily is in the hospital, giving birth to their daughter. Jake is by her side, holding her hand and encouraging her."

                                lily "(panting) I can do this."

                                michael "(whispering) You're doing great, Emily."

                                "INT. lily AND MICHAEL'S APARTMENT - DAY"

                                "lily and Michael are sitting on the couch, exhausted but happy, with their newborn daughter sleeping in a bassinet beside them."

                                lily "(smiling) She's perfect."

                                michael "(grinning) Yeah, she is."

                                "Emily and Jake kiss as their daughter peacefully sleeps beside them."

                                hide imgm

            "Emma":
                "Michael, a bright-eyed and eager 18-year-old guy, walks around the college campus, excited to start his new journey. He spots a beautiful and smart girl named Emma, who catches his attention. Emma is friendly and kind person who is loved by everyone."
                
                michael "(to himself) Wow, who is that girl? She seems so smart and confident."
                

                "Michael goes about his day, but he keeps running into Emma. They have a few brief conversations, and Michael finds himself drawn to her. He can't stop thinking about her. "

                "A few days later, Michael is running late for class and accidentally bumps into Emma, causing her to drop her books. Emma quickly offers her hand to help him pick up the books, and they exchange a few words before going their separate ways. Michael is happy to have interacted with Emma and starts having feelings for her. "

                "Days pass, and Michael and Emma start seeing each other more often. They hang out together, and Michael falls deeply in love with her. One night, they take their relationship to the next level and have their first sexual experience together. "

                
                michael "(whispering) Emma, are you sure you want to do this?"
                

                emma "(smiling) Yes, I'm sure."

                menu:
                    "Michael and Emma have decided to take their relationship to the next level and have their first sexual experience together. However, during their intimacy, Emma struggles to get excited and becomes upset."
                    "Does not explain the situation":
                        "Michael is confused and insecure, thinking that Emma isn't feeling the same way he is."

                        
                        emma "(muttering to himself) Why is this happening? I can't get excited."
                        

                        "Emma explains the situation to Michael, and they decide to research the issue."

                        "INT. EMMA'S ROOM - DAY"

                        "Michael and Emma are researching sexual dysfunction on Emma's laptop. They also reach out to their parents and friends for advice."

                        image imgo = "images/Clinic.png"
                        show imgo

                        "INT. DOCTOR'S OFFICE - DAY"

                        "Michael and Emma visit a doctor who explains the situation to them. The doctor tells them that sexual dysfunction is quite common and normal among young people and suggests some prescriptions for Emma."
                        
                        "The doctor also advises them to be patient and communicate with each other. He reassures them that this is a treatable condition and there is nothing to be ashamed of."

                        hide imgo
                        image imgt = "images/11636386596ectvdfgg626gwvk2qewkwxiiutprfsukyrdxwp0trkb0hd8do7auzvb95fc4zg4yilwkftnlshhnsbo3bo3vaz4nvujxtmsapisq.png"
                        show imgt

                        "INT. Emma'S ROOM - NIGHT"

                        "Emma takes the prescribed medication, and she and Michael try again. This time, it is a success, and they both feel happy and satisfied."

                        hide imgt
                        image imgu = "images/VihanR.png"
                        show imgu

                        "INT. MICHAEL'S DORM ROOM - DAY"

                        "Michael and Emma discuss their journey and how they overcame the problem together. They realize that communication and understanding are key to a healthy relationship."

                        hide imgu
                        image imgw = "images/11636386596ectvdfgg626gwvk2qewkwxiiutprfsukyrdxwp0trkb0hd8do7auzvb95fc4zg4yilwkftnlshhnsbo3bo3vaz4nvujxtmsapisq.png"
                        show imgw

                        "INT. EMMA'S ROOM - DAY"

                        "Emma tells Michael that she loves him and wants to spend the rest of her life with him. Michael reciprocates her feelings, and they decide to take their relationship to the next level and have a happy family."
                        
                        hide imgw

hide imgs
hide imgp
hide imgq
hide imgr

image ingv = "images/Field.png"
show ingv

label ending:
    child "Wow, I can't believe how much I've learned about conscious relationships and sexual education from this game!"

    friend "That's great to hear! What are some of the key takeaways you got from playing?"

    child "Well, I learned that it's important to communicate with my partner about what I want and what makes me feel comfortable. And I also learned about consent, and how it's important to make sure everyone involved is on the same page."

    friend "Those are really important lessons to learn. Do you think you'll be able to apply them in real life?"

    child "Definitely! I feel much more confident now that I know what to do and what to expect."

    friend "That's great to hear. And remember, if you ever have any questions or need any help, there are always resources available to you. It's important to keep learning and growing in this area throughout your life."

    child "Thanks for all your help. I feel much more prepared now!"

    friend "You're welcome! And congratulations on completing the game. You should be proud of all the progress you've made."