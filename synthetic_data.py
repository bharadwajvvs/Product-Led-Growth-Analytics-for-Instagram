import numpy as np
import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of samples to generate
num_samples = 100000

gender_options = ['Male', 'Female', 'Other']
location_options = ['US', 'UK', 'India', 'Canada', 'Australia', 'Germany', 'Brazil', 'South Africa', 'Japan', 'Mexico', 'France', 'Russia', 'China', 'Italy', 'Spain']
topic_preferences_options = ['Sports', 'Fashion', 'Tech', 'Gaming', 'Travel', 'Food', 'Music', 'Art', 'Fitness', 'Politics', 'Business', 'Science', 'Education', 'Health', 'Movies']


data = {
    'user_id': np.arange(1, num_samples + 1),
    'signup_date': [fake.date_between(start_date='-3y', end_date='today') for _ in range(num_samples)],
    'age': np.random.randint(13, 65, num_samples),
    'gender': np.random.choice(gender_options, num_samples),
    'location': np.random.choice(location_options, num_samples),
    'daily_active_users': np.random.randint(1, 31, num_samples),
    'content_views': np.random.randint(1, 3000, num_samples),
    'likes_given': np.random.randint(0, 500, num_samples),
    'comments_made': np.random.randint(0, 150, num_samples),
    'shares': np.random.randint(0, 500, num_samples),
    'direct_messages_sent': np.random.randint(0, 200, num_samples),
    'posts_created': np.random.randint(0, 50, num_samples),
    'stories_created': np.random.randint(0, 70, num_samples),
    'reels_created': np.random.randint(0, 15, num_samples),
    'followers_count': np.random.randint(0, 100000, num_samples),
    'following_count': np.random.randint(0, 5000, num_samples),
    'uses_explore': np.random.choice([True, False], num_samples),
    'uses_shopping': np.random.choice([True, False], num_samples),
    'uses_igtv': np.random.choice([True, False], num_samples),
    'uses_reels': np.random.choice([True, False], num_samples),
    'uses_stories': np.random.choice([True, False], num_samples),
    'story_views': np.random.randint(0, 12000, num_samples),
    'reel_views': np.random.randint(0, 1000000, num_samples),
    'in_app_purchases': np.round(np.random.uniform(0, 500, num_samples), 2),
    'ads_clicked': np.random.randint(0, 100, num_samples),
    'ads_viewed': np.random.randint(0, 200, num_samples),
    'in-app_message': np.random.choice([True, False], num_samples),
    'posts_viewed': np.random.randint(1, 1000, num_samples),
    'posts_you_re_not_interested_in': np.random.randint(0, 100, num_samples),
    'suggested_accounts_viewed': np.random.randint(0, 200, num_samples),
    'videos_watched': np.random.randint(0, 1000, num_samples),
    'apps_and_websites_type_off_of_instagram': np.random.choice(['Social Media', 'Blog', 'E-commerce', 'News', 'Entertainment', 'Education'], num_samples),
    'topic_preferences': [random.sample(topic_preferences_options, k=np.random.randint(1, 8)) for _ in range(num_samples)],
    'sponsored_content_engagement': np.random.randint(0, 50, num_samples),
    'churned': np.random.choice([True, False], num_samples),
    'returning_user': np.random.choice([True, False], num_samples),
    'viral_invites_sent': np.random.randint(0, 10, num_samples),
    'time_to_first_post': np.round(np.random.uniform(0, 30, num_samples), 1),
    'time_to_first_story': np.round(np.random.uniform(0, 30, num_samples), 1),
    'test_group': np.random.choice(['Control', 'Variant A', 'Variant B'], num_samples),
    'conversion_rate': np.round(np.random.uniform(0, 0.2, num_samples), 2),
    'engagement_increase': np.round(np.random.uniform(-0.2, 0.5, num_samples), 2),
}


df = pd.DataFrame(data)

df.to_csv('synthetic_instagram_plg_data.csv', index=False)
