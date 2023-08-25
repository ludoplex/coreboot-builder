web: bundle exec rails db:migrate && bundle exec rails config:read && bundle exec rails server -p $PORT
worker: celery -A your_project_name worker --loglevel=info
