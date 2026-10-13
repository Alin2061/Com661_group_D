<<<<<<< HEAD
import random 
import json

def generate_data():

    towns = ['London','Liverpool', 'Camden', 'Ilford',
             'Manchester','Richmond','Portsmouth', 'Worthing',
             'Belfast','Tower Hill']
    
    reviews_text = ['Good service', 'Poor service', 'Would not recommend', 'Could be better', 'Not worth the price', 'Excellent product',
                    'Rude staff', 'Friendly staff', 'Good place, Worth the visit']
    
    usernames = ['user1','user2','user3','user4','user5','user6','user7','user8','user9','user0',]

    business_list = []

=======
import random
import json

def generate_data():
    
    towns = ['London','Liverpool', 'Camden', 'Ilford',
            'Manchester','Richmond','Portsmouth', 'Worthing',
            'Belfast','Tower Hill']
    
    reviews_text = ['Good service', 'Poor service', 
                    'Would not recommend', 'Could be better', 
                    'Not worth the price', 'Excellent product',
                    'Rude staff', 'Friendly staff', 
                    'Good place, Worth the visit']
    
    usernames = ['user1','user2','user3','user4','user5',
                 'user6','user7','user8','user9','user0',]
    
    
    business_list = []
    
>>>>>>> bab87b110ef9c02d0c2556b3326af5d10f1457f0
    for i in range(100):
        name = "Biz" + str(i)
        town = random.choice(towns)
        rating = random.randint(1,5)
        reviews = []
<<<<<<< HEAD

=======
        
>>>>>>> bab87b110ef9c02d0c2556b3326af5d10f1457f0
        for _ in range(random.randint(2,3)):
            username = random.choice(usernames)
            review = random.choice(reviews_text)
            stars = random.randint(1,5)
<<<<<<< HEAD

            reviews.append({
                "username" : username,
                "comments" : review,
                "stars" : stars
            })

        business_list.append({
            "name" : name,
            "town" : town,
            "rating" : rating,
            "reviews" : reviews
        })

=======
            
            reviews.append({
                "username" : username,
                "comments" : review,
                "stars": stars
            })
        
        business_list.append({
            "name": name,
            "town": town,
            "rating": rating,
            "reviews": reviews
        })
    
>>>>>>> bab87b110ef9c02d0c2556b3326af5d10f1457f0
    return business_list

business = generate_data()

with open('data.json', 'w', encoding='utf-8') as fout:
    json.dump(business, fout, indent=4)