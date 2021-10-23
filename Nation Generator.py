# A hoi4 nation generator for the Final Fading Flame Mod
# This will create a txt file wherever this script is stored,
# containing all of the bare-bones basic info that a country needs
# to be properly instantiated in the Final Fading Flame Mod
# By Narkoth
import os

def gen(tag, name, r_value, g_value, b_value, capital_state):
    tag = tag.upper()
    with open((tag + " - " + name + ".txt"), "w") as file:
              countries = "###########################\n\n"
              countries = countries + "# Place Below in a new countries file"
              countries = countries + "\ngraphical_culture = eastern_european_gfx\ngraphical_culture_2d = eastern_european_2d"
              countries = countries + "\ncolor = { " + r_value + " " + g_value + " " + b_value + " }"
              file.write(countries)
              country_color = "\n\n###########################\n\n"
              country_color = country_color + "#Place below in the countries colors txt file\n"
              country_color = country_color + tag + " =  {" + " color = rgb { " + r_value +  " " + g_value + " " + b_value + " }"
              country_color = country_color + " color_ui = rgb { " + r_value +  " " + g_value + " " + b_value + " }  }"
              file.write(country_color)
              country_tags = "\n\n###########################\n\n"
              country_tags = country_tags + "#Place below in the country_tags file\n"
              country_tags = country_tags + "" + tag + " =" + ' "' + "countries" + "/" + tag + ".txt" + '"'
              file.write(country_tags)
              history_file = "\n\n###########################\n\n"
              history_file = history_file + "#Place below in a new history file\n"
              history_file = history_file + "capital = " + capital_state + "\n"
              history_file = history_file + "oob = " + '"' + tag + '_land"\n'
              history_file = history_file + "set_stability = 0.50\n"
              history_file = history_file + "set_war_support = 0.10\n"
              history_file = history_file + "set_research_slots = 2\n"
              history_file = history_file + "set_convoys = 100\n"
              history_file = history_file + "set_technology = {\n"
              history_file = history_file + "	infantry_weapons = 1\n"
              history_file = history_file + "	tech_support = 1\n"
              history_file = history_file + "	gw_artillery = 1\n"
              history_file = history_file + "	gwtank  = 1\n"
              history_file = history_file + "	early_fighter  = 1\n"
              history_file = history_file + "	early_bomber  = 1\n"
              history_file = history_file + "}\n"
              history_file = history_file + "if = {\n"
              history_file = history_file + "	limit = { not = { has_dlc = " + '"Man the Guns"' + " } }\n"
              history_file = history_file + "	set_technology = {\n"
              history_file = history_file + "		early_destroyer = 1\n"
              history_file = history_file + "		early_light_cruiser = 1\n"
              history_file = history_file + "		early_heavy_cruiser = 1\n"
              history_file = history_file + "		transport = 1\n"
              history_file = history_file + "		early_submarine = 1\n"
              history_file = history_file + "	}\n"
              history_file = history_file + "	#Set a naval OOB here if it is appropriate for this nation\n"
              history_file = history_file + "}\n"
              history_file = history_file + "if = {\n"
              history_file = history_file + "	limit = { has_dlc = " + '"Man the Guns"' + " }\n"
              history_file = history_file + "	set_technology = {\n"
              history_file = history_file + "		basic_naval_mines = 1\n"
              history_file = history_file + "		early_ship_hull_light = 1\n"
              history_file = history_file + "		early_ship_hull_submarine = 1\n"
              history_file = history_file + "		early_ship_hull_cruiser = 1\n"
              history_file = history_file + "		basic_battery = 1\n"
              history_file = history_file + "		basic_secondary_battery = 1\n"
              history_file = history_file + "		basic_torpedo = 1\n"
              history_file = history_file + "		basic_depth_charges = 1\n"
              history_file = history_file + "		mtg_transport = 1\n"
              history_file = history_file + "		sonar = 1\n"
              history_file = history_file + "	}\n"
              history_file = history_file + "	#Set a naval OOB here if it is appropriate for this nation\n"
              history_file = history_file + "}\n"
              history_file = history_file + "set_politics = {\n"
              history_file = history_file + "	ruling_party = centrism\n"
              history_file = history_file + "	last_election = " + '"98.1.1"' + "\n"
              history_file = history_file + "	election_frequency = 48\n"
              history_file = history_file + "	elections_allowed = no\n"
              history_file = history_file + "}\n"
              history_file = history_file + "set_popularities = {\n"
              history_file = history_file + "	centrism = 100\n"
              history_file = history_file + "}\n"
              file.write(history_file)
              oob = "\n\n###########################\n\n"
              oob = oob + "#Place the following in a new land OOB file\n"
              oob = oob + "division_template = {\n"
              oob = oob + "	name = " + '"Infantry Division"' + "\n"
              oob = oob + "	regiments = {\n"
              oob = oob + "		infantry = { x = 0 y = 0 }\n"
              oob = oob + "		infantry = { x = 0 y = 1 }\n"
              oob = oob + "		infantry = { x = 1 y = 0 }\n"
              oob = oob + "		infantry = { x = 1 y = 1 }\n"
              oob = oob + "		infantry = { x = 2 y = 0 }\n"
              oob = oob + "		infantry = { x = 2 y = 1 }\n"
              oob = oob + "	}\n"
              oob = oob + "}\n"
              file.write(oob)
              gen_local(tag, name)

def gen_local(tag, name):
    tag = tag.upper()
    with open((tag + " - LOCALIZATION "+ ".txt"), "w") as file:
              ideologies = ["full_theocracy", "rationalist_theocracy", "statism", "totalitarianism",
                            "nationalism", "governism", "unitary_corporatism", "corporate_feudalism",
                            "liberated_corporatism", "partnerism", "guildism", "unionism", "classical_communalism",
                            "anarcho_marxism", "imperialism", "monarchism", "divine_right_monarchism", "constitutional_monarchism",
                            "revanchism", "republicanism", "uniform_statism", "federalism", "centrism", "democratism", "libertarianism",
                            "utopianism", "just_worldism", "isolationism", "cooperativism"]
              for ideo in ideologies:
                  line = tag + "_" + ideo + ":0 " + '"' + name + '"\n'
                  file.write(line)
                  line1 = tag + "_" + ideo + "_DEF:0 " + '"the ' + name + '"\n'
                  file.write(line1)
                  line2 = tag + "_" + ideo + "_ADJ:0 " + '"' + name + '"\n'
                  file.write(line2)
              generic_name = tag + ":0 " + '"' + name + '"\n'
              file.write(generic_name)
              generic_def = tag + "_DEF:0 " + '"' + name + '"\n'
              file.write(generic_def)
              generic_adj = tag + "_ADJ:0 " + '"' + name + '"'
              file.write(generic_adj)

def main():
    print("Hello! Please enter the following information without any additional spaces, merely hit enter after you are done typing ...\n")
    print("Enter the tag of the nation you want to create: ")
    tag = str(input())
    print("\nEnter the name of the nation, with no political affiliation tied to it, like England")
    name = str(input())
    print("\nEnter the R value of the RGB value for the color of the nation:")
    r_value = str(input())
    print("\nEnter the G value of the RGB value for the color of the nation:")
    g_value = str(input())
    print("\nEnter the B value of the RGB value for the color of the nation:")
    b_value = str(input())
    print("\nEnter the capital state ID of the nation in question:")
    capital_state = str(input())
    print("\nExcellent! Two files will now be generated that will provide the basic code for your new hoi4 nation.")
    print("\nHit enter to execute the script and close this window")
    gen(tag, name, r_value, g_value, b_value, capital_state)
              
              
    
