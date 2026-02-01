import csv
import random
from pathlib import Path

# Set random seed for reproducibility
random.seed(42)

# Define realistic first and last names
first_names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery", "Quinn",
    "Jamie", "Sam", "Drew", "Cameron", "Peyton", "Skyler", "Reese", "Harper",
    "Finley", "Rowan", "Dakota", "Sage", "River", "Phoenix", "Kai", "Emerson",
    "Hayden", "Kendall", "Logan", "Madison", "Parker", "Ryan", "Blake", "Devon",
    "Elliott", "Frankie", "Gray", "Hollis", "Indigo", "Jules", "Kirby", "Lane",
    "Marley", "Nico", "Oakley", "Palmer", "Quincy", "Remy", "Sawyer", "Tatum",
    "Valencia", "Winter", "Arden", "Blair", "Charlie", "Dylan", "Eden", "Finch"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker"
]

# Define roles for each team
team_roles = {
    "BET Digital": [
        "Social Media Manager", "Content Creator", "Video Editor", "Graphic Designer",
        "Community Manager", "Digital Strategist", "Creative Director", "Producer",
        "Motion Designer", "Copywriter", "Brand Manager"
    ],
    "Paramount Plus Brand Creative": [
        "Brand Designer", "Art Director", "Motion Graphics Designer", "Creative Strategist",
        "Visual Designer", "UX Designer", "Copywriter", "Video Producer", "Animator",
        "Marketing Designer", "Campaign Manager"
    ],
    "Data Insights and Research": [
        "Data Analyst", "Research Analyst", "Data Scientist", "Business Intelligence Analyst",
        "Analytics Manager", "Data Engineer", "Insights Specialist", "Quantitative Researcher",
        "SQL Developer", "Dashboard Developer"
    ],
    "The Multiplatform Group": [
        "Content Strategist", "Platform Manager", "Digital Producer", "Social Media Specialist",
        "Multi-platform Editor", "Content Coordinator", "Distribution Manager", "Audience Developer"
    ],
    "Nickelodeon Digital": [
        "Kids Content Creator", "Animation Designer", "Social Media Manager", "Video Editor",
        "Graphic Designer", "Digital Producer", "Community Manager", "Creative Lead",
        "Motion Designer", "Brand Manager"
    ],
    "CBS Marketing": [
        "Marketing Manager", "Promo Producer", "Editor", "Videographer", "Marketing Coordinator",
        "Campaign Strategist", "Media Buyer", "Brand Specialist", "Content Producer",
        "Creative Services Manager", "Avid Editor"
    ],
    "Editorial Post Production Operations": [
        "Post Production Supervisor", "Video Editor", "Assistant Editor", "Post Coordinator",
        "Workflow Manager", "Media Manager", "Quality Control Specialist", "Encoder",
        "Archive Specialist", "Operations Manager"
    ]
}

# All 7 AI tools
tools = [
    "Runway ML", "Google Gemini", "Adobe Firefly", "ChatGPT",
    "Microsoft Copilot", "Claude AI", "Cursor"
]

def generate_usage_data(team_name, team_size):
    """
    Generate realistic usage data based on team characteristics.
    
    Parameters:
    - team_name: Name of the team
    - team_size: Number of people on the team
    
    Returns: List of dictionaries with usage data
    """
    
    data = []
    used_names = set()
    
    for _ in range(team_size):
        # Generate unique name
        while True:
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            if name not in used_names:
                used_names.add(name)
                break
        
        # Assign role
        role = random.choice(team_roles[team_name])
        
        # Generate data for each tool
        for tool in tools:
            # Base values (will be adjusted per team/tool)
            satisfaction = 3
            usage = 2
            
            # CHATGPT: Most popular overall, but limited at work
            if tool == "ChatGPT":
                satisfaction = random.randint(3, 5)  # Generally well-liked
                usage = random.randint(1, 3)  # Low work usage (not allowed)
                # Personal use boost
                if random.random() < 0.7:  # 70% use it personally
                    usage = min(usage + random.randint(1, 2), 4)
            
            # ADOBE FIREFLY: High for creative teams
            elif tool == "Adobe Firefly":
                if team_name in ["BET Digital", "Nickelodeon Digital", "Paramount Plus Brand Creative"]:
                    satisfaction = random.randint(4, 5)
                    usage = random.randint(3, 5)
                else:
                    satisfaction = random.randint(2, 4)
                    usage = random.randint(0, 2)
            
            # GOOGLE GEMINI: Paramount Plus preference
            elif tool == "Google Gemini":
                if team_name == "Paramount Plus Brand Creative":
                    satisfaction = random.randint(4, 5)
                    usage = random.randint(3, 5)
                else:
                    satisfaction = random.randint(2, 4)
                    usage = random.randint(0, 2)
            
            # CLAUDE AI: Data team uses personally
            elif tool == "Claude AI":
                if team_name == "Data Insights and Research":
                    satisfaction = random.randint(4, 5)
                    usage = random.randint(2, 4)  # Personal use
                else:
                    satisfaction = random.randint(2, 4)
                    usage = random.randint(0, 2)
            
            # CURSOR: New tool, Data team experimenting
            elif tool == "Cursor":
                if team_name == "Data Insights and Research":
                    satisfaction = random.randint(3, 5)
                    usage = random.randint(1, 3)  # Just allowed, experimenting
                else:
                    satisfaction = random.randint(1, 3)
                    usage = random.randint(0, 1)  # Very low usage elsewhere
            
            # MICROSOFT COPILOT: EPPO team uses due to SharePoint
            elif tool == "Microsoft Copilot":
                if team_name == "Editorial Post Production Operations":
                    satisfaction = random.randint(2, 3)  # Dislikes Microsoft but uses it
                    usage = 3  # Average 3 days a week
                    # Add some variation
                    usage = max(0, min(7, usage + random.randint(-1, 1)))
                else:
                    satisfaction = random.randint(1, 3)
                    usage = random.randint(0, 1)
            
            # RUNWAY ML: Creative/video teams
            elif tool == "Runway ML":
                if team_name in ["BET Digital", "Nickelodeon Digital", "Paramount Plus Brand Creative", "Editorial Post Production Operations"]:
                    satisfaction = random.randint(3, 5)
                    usage = random.randint(2, 4)
                else:
                    satisfaction = random.randint(1, 3)
                    usage = random.randint(0, 2)
            
            # CBS Marketing: More traditional, AI-wary at work
            if team_name == "CBS Marketing":
                # Reduce work usage for all tools
                if tool != "ChatGPT":  # ChatGPT they use personally
                    usage = max(0, usage - 2)
                    satisfaction = max(1, satisfaction - 1)
            
            # Add natural variation (some people just don't use tools much)
            if random.random() < 0.2:  # 20% are non-users
                usage = 0
                satisfaction = random.randint(0, 2)
            
            # Ensure values stay in range
            satisfaction = max(0, min(5, satisfaction))
            usage = max(0, min(7, usage))
            
            data.append({
                "User Name": name,
                "Role": role,
                "Product": tool,
                "User Satisfaction (0-5)": satisfaction,
                "Weekly Usage (0-7)": usage,
                "Team": team_name
            })
    
    return data

# Generate CSV for each team
teams = {
    "BET Digital": 65,
    "Paramount Plus Brand Creative": 40,
    "Data Insights and Research": 45,
    "The Multiplatform Group": 50,
    "Nickelodeon Digital": 60,
    "CBS Marketing": 80,
    "Editorial Post Production Operations": 35
}

# Create output directory
output_dir = Path("/Users/lawhea1214/Documents/portfolio/data_analysis/utilization/data")
output_dir.mkdir(exist_ok=True)

for team_name, team_size in teams.items():
    # Generate data
    team_data = generate_usage_data(team_name, team_size)
    
    # Create safe filename
    filename = team_name.replace(" ", "_") + ".csv"
    filepath = output_dir / filename
    
    # Write to CSV
    with open(filepath, 'w', newline='') as csvfile:
        fieldnames = ["User Name", "Role", "Product", "User Satisfaction (0-5)", 
                     "Weekly Usage (0-7)", "Team"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(team_data)
    
    print(f"✓ Created {filename} with {len(team_data)} rows ({team_size} people × 7 tools)")

print(f"\n🎉 All files saved to: {output_dir}")
