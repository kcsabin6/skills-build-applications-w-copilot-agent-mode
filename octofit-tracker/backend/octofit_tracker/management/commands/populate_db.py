from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')

        try:
            # Create users
            users = []
            user_data = [
                {'username': 'thundergod', 'email': 'thundergod@mhigh.edu', 'password': 'thundergodpassword'},
                {'username': 'metalgeek', 'email': 'metalgeek@mhigh.edu', 'password': 'metalgeekpassword'},
                {'username': 'zerocool', 'email': 'zerocool@mhigh.edu', 'password': 'zerocoolpassword'},
                {'username': 'crashoverride', 'email': 'crashoverride@mhigh.edu', 'password': 'crashoverridepassword'},
                {'username': 'sleeptoken', 'email': 'sleeptoken@mhigh.edu', 'password': 'sleeptokenpassword'},
            ]
            for data in user_data:
                user = User(_id=ObjectId(), **data)
                user.save()
                users.append(user)
            self.stdout.write('Users created successfully.')

            # Create teams
            team1 = Team(_id=ObjectId(), name='Blue Team')
            team2 = Team(_id=ObjectId(), name='Gold Team')
            team1.save()
            team2.save()
            team1.members.add(users[0], users[1])
            team2.members.add(users[2], users[3], users[4])
            self.stdout.write('Teams created successfully.')

            # Create activities
            activity_data = [
                {'user': users[0], 'activity_type': 'Cycling', 'duration': timedelta(hours=1)},
                {'user': users[1], 'activity_type': 'Crossfit', 'duration': timedelta(hours=2)},
                {'user': users[2], 'activity_type': 'Running', 'duration': timedelta(hours=1, minutes=30)},
                {'user': users[3], 'activity_type': 'Strength', 'duration': timedelta(minutes=30)},
                {'user': users[4], 'activity_type': 'Swimming', 'duration': timedelta(hours=1, minutes=15)},
            ]
            for data in activity_data:
                activity = Activity(_id=ObjectId(), **data)
                activity.save()
            self.stdout.write('Activities created successfully.')

            # Create leaderboard entries
            leaderboard_data = [
                {'user': users[0], 'score': 100},
                {'user': users[1], 'score': 90},
                {'user': users[2], 'score': 95},
                {'user': users[3], 'score': 85},
                {'user': users[4], 'score': 80},
            ]
            for data in leaderboard_data:
                leaderboard = Leaderboard(_id=ObjectId(), **data)
                leaderboard.save()
            self.stdout.write('Leaderboard entries created successfully.')

            # Create workouts
            workout_data = [
                {'name': 'Cycling Training', 'description': 'Training for a road cycling event'},
                {'name': 'Crossfit', 'description': 'Training for a crossfit competition'},
                {'name': 'Running Training', 'description': 'Training for a marathon'},
                {'name': 'Strength Training', 'description': 'Training for strength'},
                {'name': 'Swimming Training', 'description': 'Training for a swimming competition'},
            ]
            for data in workout_data:
                workout = Workout(_id=ObjectId(), **data)
                workout.save()
            self.stdout.write('Workouts created successfully.')

            self.stdout.write(self.style.SUCCESS('Database population completed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during database population: {e}'))