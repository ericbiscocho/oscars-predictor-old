#!/bin/bash
# Import csv files into data-cleanedbase

# Oscars collection
mongoimport --type csv -d oscars -c best_actor --headerline --drop ../part1/data-cleaned/oscars/best_actor.csv
mongoimport --type csv -d oscars -c best_actor_supporting --headerline --drop ../part1/data-cleaned/oscars/best_actor_supporting.csv
mongoimport --type csv -d oscars -c best_actress --headerline --drop ../part1/data-cleaned/oscars/best_actress.csv
mongoimport --type csv -d oscars -c best_actress_supporting --headerline --drop ../part1/data-cleaned/oscars/best_actress_supporting.csv
mongoimport --type csv -d oscars -c best_director --headerline --drop ../part1/data-cleaned/oscars/best_director.csv
mongoimport --type csv -d oscars -c best_picture --headerline --drop ../part1/data-cleaned/oscars/best_picture.csv
mongoimport --type csv -d oscars -c best_screenplay_adapted --headerline --drop ../part1/data-cleaned/oscars/best_screenplay_adapted.csv
mongoimport --type csv -d oscars -c best_screenplay_original --headerline --drop ../part1/data-cleaned/oscars/best_screenplay_original.csv

# BAFTA collection
mongoimport --type csv -d bafta -c best_actor --headerline --drop ../part1/data-cleaned/bafta/best_actor.csv
mongoimport --type csv -d bafta -c best_actor_supporting --headerline --drop ../part1/data-cleaned/bafta/best_actor_supporting.csv
mongoimport --type csv -d bafta -c best_actress --headerline --drop ../part1/data-cleaned/bafta/best_actress.csv
mongoimport --type csv -d bafta -c best_actress_supporting --headerline --drop ../part1/data-cleaned/bafta/best_actress_supporting.csv
mongoimport --type csv -d bafta -c best_direction --headerline --drop ../part1/data-cleaned/bafta/best_direction.csv
mongoimport --type csv -d bafta -c best_film --headerline --drop ../part1/data-cleaned/bafta/best_film.csv
mongoimport --type csv -d bafta -c best_screenplay_adapted --headerline --drop ../part1/data-cleaned/bafta/best_screenplay_adapted.csv
mongoimport --type csv -d bafta -c best_screenplay_original --headerline --drop ../part1/data-cleaned/bafta/best_screenplay_original.csv

# Guilds collection
mongoimport --type csv -d guilds -c best_actor --headerline --drop ../part1/data-cleaned/sag/best_actor.csv
mongoimport --type csv -d guilds -c best_actor_supporting --headerline --drop ../part1/data-cleaned/sag/best_actor_supporting.csv
mongoimport --type csv -d guilds -c best_actress --headerline --drop ../part1/data-cleaned/sag/best_actress.csv
mongoimport --type csv -d guilds -c best_actress_supporting --headerline --drop ../part1/data-cleaned/sag/best_actress_supporting.csv
mongoimport --type csv -d guilds -c best_feature_film --headerline --drop ../part1/data-cleaned/dga/best_feature_film.csv
mongoimport --type csv -d guilds -c best_motion_picture --headerline --drop ../part1/data-cleaned/pga/best_motion_picture.csv
mongoimport --type csv -d guilds -c best_screenplay_adapted --headerline --drop ../part1/data-cleaned/wga/best_screenplay_adapted.csv
mongoimport --type csv -d guilds -c best_screenplay_original --headerline --drop ../part1/data-cleaned/wga/best_screenplay_original.csv