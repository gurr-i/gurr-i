import re

# Read the original template
with open('template.svg', 'r') as f:
    content = f.read()

# Add gradient definitions after the template_settings
gradient_defs = '''
        <!-- Animated Gradient Background -->
        <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{{ theme.back }};stop-opacity:1">
                <animate attributeName="stop-color" values="{{ theme.back }};{{ theme.purple }};{{ theme.back }}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" style="stop-color:{{ theme.purple }};stop-opacity:0.6">
                <animate attributeName="stop-color" values="{{ theme.purple }};{{ theme.cyan }};{{ theme.purple }}" dur="6s" repeatCount="indefinite" />
            </stop>
        </linearGradient>
        
        <!-- Glow Effect -->
        <radialGradient id="glowGradient" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:{{ theme.orange }};stop-opacity:0.8">
                <animate attributeName="stop-opacity" values="0.8;0.3;0.8" dur="3s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" style="stop-color:{{ theme.back }};stop-opacity:0" />
        </radialGradient>
        
        <!-- Particle System -->
        <filter id="particleGlow">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <!-- 3D Shadow Effect -->
        <filter id="dropShadow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="3" />
            <feOffset dx="2" dy="2" result="offsetblur"/>
            <feFlood flood-color="{{ theme.purple }}" flood-opacity="0.3"/>
            <feComposite in2="offsetblur" operator="in"/>
            <feMerge>
                <feMergeNode/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>'''

# Insert gradient definitions
content = content.replace('</termtosvg:template_settings>', '</termtosvg:template_settings>' + gradient_defs)

# Replace background rect with gradient background
content = content.replace(
    '<rect id="terminalui" class="background" width="100%" height="100%" ry="4.5826941" />',
    '<rect id="terminalui" fill="url(#bgGradient)" width="100%" height="100%" ry="4.5826941" filter="url(#dropShadow)" />'
)

# Add interactive hover effects to the terminal window
content = content.replace(
    '<rect id="terminalui" fill="url(#bgGradient)" width="100%" height="100%" ry="4.5826941" filter="url(#dropShadow)" />',
    '''<rect id="terminalui" fill="url(#bgGradient)" width="100%" height="100%" ry="4.5826941" filter="url(#dropShadow)">
            <animateTransform attributeName="transform" type="scale" values="1;1.02;1" dur="4s" repeatCount="indefinite" />
        </rect>'''
)

# Add particle effects circles
particle_effects = '''
    <!-- Particle Effects -->
    <circle cx="25" cy="25" r="2" fill="{{ theme.orange }}" opacity="0.6" filter="url(#particleGlow)">
        <animate attributeName="cy" values="25;400;25" dur="6s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.6;0.1;0.6" dur="6s" repeatCount="indefinite" />
    </circle>
    <circle cx="475" cy="50" r="1.5" fill="{{ theme.cyan }}" opacity="0.5" filter="url(#particleGlow)">
        <animate attributeName="cy" values="50;380;50" dur="8s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.5;0.1;0.5" dur="8s" repeatCount="indefinite" />
    </circle>
    <circle cx="250" cy="30" r="1" fill="{{ theme.green }}" opacity="0.7" filter="url(#particleGlow)">
        <animate attributeName="cy" values="30;390;30" dur="5s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.7;0.2;0.7" dur="5s" repeatCount="indefinite" />
    </circle>'''

# Insert particle effects before the closing svg tag
content = content.replace('</svg>', particle_effects + '\n</svg>')

# Add 3D transform to the screen animation
content = content.replace(
    'animation-name:roll;',
    'animation-name:roll;\n                transform-style: preserve-3d;\n                perspective: 1000px;'
)

# Add hover interactions
interactive_style = '''
            /* Interactive hover effects */
            #terminalui:hover {
                filter: url(#dropShadow) brightness(1.2);
                transition: filter 0.3s ease;
            }
            
            #screen_view:hover {
                transform: scale(1.02) rotateX(5deg);
                transition: transform 0.3s ease;
            }'''

# Add interactive styles
content = content.replace('</style>', interactive_style + '\n        </style>')

# Write the enhanced template
with open('template_enhanced.svg', 'w') as f:
    f.write(content)

print("Enhanced template created successfully!")
