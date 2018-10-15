import pandas as pd
from datetime import datetime


allmovie_genres = ["Action","Adult","Adventure","Avant-garde / Experimental","Business","Children's/Family","Comedy","Comedy Drama","Crime","Culture & Society","Dance","Drama","Education","Epic","Family & Personal Relationships","Fantasy","Health & Fitness","Historical Film","Language & Literature","Leisure Arts","Music","Musical","Horror","Mystery","Nature","News","Reality Show","Romance","Science Fiction","Spirituality & Philosophy","Sports & Recreation","Spy Film","Theater","Thriller","Travel","Visual Arts","War","Western"]
allmovie_subgenres = ["Action Comedy","Action Thriller","Biker Film","Blaxploitation","Chase Movie","Chase/Road Show","Disaster Film","Escape Film","Martial Arts","Road Movie","Romantic Adventure","Samurai Film","Superhero Film","Superhero Show","Swashbuckler","Adult Entertainment","Hardcore Sex Film","Hentai","Sexploitation","Softcore Pay-Cable Show","Softcore Sex Film","Adventure Comedy","Adventure Drama","Costume Adventure","Jungle Film","Sea Adventure","Abstract Film","Essay Film","Surrealist Film","Computers","Finance & Investing","Sales & Marketing","Small Business","Workplace Issues","Animal Picture","Children's Entertainment","Children's Fantasy","Fairy Tales & Legends","Family-Oriented Adventure","Family-Oriented Comedy","Absurd Comedy","Americana","Beach Film","Black Comedy","Bloopers & Candid Camera","Comedy of Errors","Comedy of Manners","Comedy Thriller","Courtroom Comedy","Domestic Comedy","Fantasy Comedy","Farce","Gross-Out Comedy","Heavenly Comedy","Media Satire","Medical Comedy","Military Comedy","Mockumentary","Musical Comedy","Parody/Spoof","Police Comedy","Prank/Candid-Camera","Religious Comedy","Romantic Comedy","Satire","Screwball Comedy","Sex Comedy","Showbiz Comedy","Sitcom","Sketch Comedy","Sketch Comedy/Skit Show","Slapstick","Sophisticated Comedy","Sports Comedy","Standup Comedy","Stoner Comedy","Urban Comedy","Workplace Comedy","Buddy Film","Buddy Show","Coming-of-Age","Early Black Cinema","Ensemble Film","Feminist Film","Gay & Lesbian Films","Gay & Lesbian Show","Holiday Film","Odd Couple Film","Political Satire","Pop-Culture Show","Reunion Films","Slice of Life","Studio-Era Black Cinema","Teen Movie","Teen Show","Tragi-comedy","Trash Film","Caper","Cop Show","Crime Comedy","Crime Drama","Crime Thriller","Detective Film","Detective Show","Film Noir","Gangster Film","Gangster Show","Juvenile Delinquency Film","Master Criminal Films","Post-Noir (Modern Noir)","Prison Film","Prison Show","Procedural Show","True Crime","True-Crime Show","Anthropology","Architecture & Design","Art History","Beauty & Fashion","Biography","Cooking & Food","Film & Television History","Gender Issues","Hobbies & Games","Interpersonal Relationships","Inventions & Innovations","Journalism","Law & Crime","Marriage & Commitment","Media Studies","Mythology","Parenting","Performance Art","Politics & Government","Psychology","Race & Ethnicity","Sexuality","Shockumentary","Social History","Social Issues","Sociology","Sports","Tragedies & Catastrophes","Trivia/Quiz Show","Variety Show","World History","Ballroom Dance","Jazz & Modern Dance","Addiction Drama","Animal Show","Anthology Series","Anti-War Film","Biopic [feature]","Childhood Drama","Courtroom Drama","Docudrama","Erotic Drama","Family Drama","Film a Clef","Heavenly Drama","Inspirational Drama","Marriage Drama","Medical Drama","Medical Show","Melodrama","Message Movie","Musical Drama","Period Show","Political Drama","Political Thriller","Prime-Time Drama","Propaganda Film","Psychological Drama","Religious Drama","Romantic Drama","Rural Drama","Showbiz Drama","Soap Opera","Social Problem Film","Sports Drama","Supernatural Drama","Telenovela","Tragedy","Urban Drama","Adult Education","Careers","Children's Educational","Children's Issues","College & Test Prep","Special Education","Teaching","Vehicles & Transportation","British Empire Film","Epic Western","Historical Epic","Religious Epic","Romantic Epic","War Epic","Gardening","Home Decoration & Improvement","Home Entertaining","Weddings","Anime","Fantasy Adventure","Fantasy Drama","Harem Anime [Anime]","Heaven-Can-Wait Fantasies","Mythological Fantasy","Prehistoric Fantasy","Sword-and-Sandal","Sword-and-Sorcery","Aerobic Exercise","Alternative Health","Ambiance","Cooking Show","Diet & Nutrition","Illnesses & Disabilities","Martial Arts","Medicine","Morality & Values","Personal Safety","Self-Help","Toning & Strength Training","Women's Health","Yoga","Hagiography","Period Film","Costume Horror","Creature Film","Haunted House Film","Horror Comedy","Natural Horror","Sadistic Horror","Sci-Fi Horror","Sex Horror","Slasher Film","Supernatural Horror","Linguistics","Literary Studies","Holidays","Lifestyle Show","Makeover Show","Concerts","Instrumental Music","Music History","Music Show","Vocal Music","Animated Musical","Backstage Musical","Ballet","Dance Film","Film-Opera","Musical Fantasy","Musical Romance","Operetta","Rock Musical","Giallo","Gothic Film","Police Detective Film","Police Drama","Poliziotteschi","Whodunit","Adventure Travel","Animals","Biological Sciences","Environmental Science","Natural Environments","Nature Show","Physical Sciences","Unexplained Phenomena","Weather","News Magazine","Panel Show","Talk Show","Awards Show","Beauty/Talent Show","Candid Reality Show","Celebrity Reality Show","Competitive Reality Show","Dating Show","Game Show","Romantic Fantasy","Romantic Mystery","War Romance","Alien Film","Psychological Sci-Fi","Sci-Fi Action","Sci-Fi Adventure","Sci-Fi Comedy","Sci-Fi Disaster Film","Space Adventure","Tech Noir","New Age & Metaphysics","Philosophy","Religions & Belief Systems","Extreme Sports","Game Broadcast","Motor Sports","Sports Show","Glamorized Spy Film","Spy Comedy","Spy Show","Unglamorized Spy Film","War Spy Film","Filmed Play","Opera","Erotic Thriller","Law Show","Paranoid Thriller","Psychological Thriller","Supernatural Thriller","Armchair Travel","Guided Travel","Outdoor Recreation","Travel Show","Audio-Visual","Graphic & Applied Arts","Sculpture","Video Art","Cavalry Film","Combat Films","Military & War","POW Drama","Resistance Film","War Adventure","War Drama","B-Western","Comedy Western","Eurowestern","Hybrid Western","Indian Western","Modern Western","Musical Western","Outlaw (Gunfighter) Film","Psychological Western","Revisionist Western","Spaghetti Western","Traditional Western"]


with open("links_all.csv","w+", encoding="utf-8") as testFile:
    testFile.write("title,genres,subGenres,releaseDate,duration,countries,mpaaRating,allmovieRating,flags,directedBy,producedBy,releasedBy,moods,themes,keywords,attributes,synopsis,actors,relatedMovies\n")
    for i in range(0,19):
        if i < 10:
            i = "0"+str(i)
        df = pd.read_csv("links_20"+str(i)+".csv", sep=",", header=None, names=["link","title","genres","subGenres","releaseDate","duration","countries","mpaaRating","allmovieRating","flags","directedBy","producedBy","releasedBy","moods","themes","keywords","attributes","synopsis","actors","relatedMovies"])
        for index, row in df.iterrows():
            link = row["link"]
            title = row["title"]
            genres = row["genres"]
            subGenres = row["subGenres"]
            releaseDate = row["releaseDate"].strip()
            try:
                releaseDate = datetime.strptime(releaseDate,"%b %d %Y")
            except Exception:
                releaseDate = datetime.strptime("20"+str(i),"%Y")
            duration = row["duration"]
            countries = row["countries"]
            mpaaRating = row["mpaaRating"]
            allmovieRating = row["allmovieRating"]
            flags = row["flags"]
            directedBy = row["directedBy"]
            producedBy = row["producedBy"]
            releasedBy = row["releasedBy"]
            moods = row["moods"]
            themes = row["themes"]
            keywords = row["keywords"]
            attributes = row["attributes"]
            synopsis = row["synopsis"]
            actors = row["actors"]
            relatedMovies = row["relatedMovies"]
            genresHit = ""
            for allmovie_genre in allmovie_genres:
                if allmovie_genre in genres and allmovie_genre not in genresHit:
                    if allmovie_genre is "Comedy":
                        if "Drama" in genres:
                            genresHit = genresHit + "Comedy | Comedy Drama | Drama | "
                        else:
                            genresHit = genresHit + "Comedy | "
                    else:
                        genresHit = genresHit + allmovie_genre + " | "
            
            subGenresHit = ""
            for allmovie_subgenre in allmovie_subgenres:
                if allmovie_subgenre in subGenres:
                    subGenresHit = subGenresHit + allmovie_subgenre + " | "

            #print("Title: " + title + "\n" + "Sub Genres: " + subGenres + "\n" + "Sub Genres Hit: " + subGenresHit[:-3])
            entry = str(title).strip() + "," + str(genresHit[:-3]).strip() + "," + str(subGenresHit[:-3]).strip() + "," + str(releaseDate).strip() + "," + str(duration).strip() + ","
            entry = entry + str(countries).strip() + "," + str(mpaaRating).strip() + "," + str(allmovieRating).strip() + "," + str(flags).strip() + "," + str(directedBy).strip() + ","
            entry = entry + str(producedBy).strip() + "," + str(releasedBy).strip() + "," + str(moods).strip() + "," + str(themes).strip() + ","
            entry = entry + str(keywords).strip() + "," + str(attributes).strip() + "," + str(synopsis).strip() + "," + str(actors).strip() + ","
            entry = entry + str(relatedMovies).strip() + "\n"
            testFile.write(entry)
            
testFile.close()
    