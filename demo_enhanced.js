const fs = require('fs')
const nunjucks = require('nunjucks')
const themes = require("./src/theme")

// Configure nunjucks
nunjucks.configure({ autoescape: true })

// Read the enhanced template
let templateString = fs.readFileSync("template_enhanced.svg", 'utf-8')

// Sample data for demonstration
const sampleData = {
    username: "octocat",
    name: "The Octocat",
    stars: "   1,234    ",
    forks: "     567    ",
    commits: "   2,890    ",
    followers: "   3,456    ",
    pr: "       123    ",
    issues: "    89    ",
    repo: "      42    ",
    gists: "    15    ",
    uptime: "1,234 days"
}

// Generate SVG with different themes for testing
const themesToTest = ['default', 'dracula', 'monokai', 'hacker', 'github']

themesToTest.forEach(themeName => {
    try {
        let outString = nunjucks.renderString(templateString, {
            data: sampleData,
            theme: themes.getTheme(themeName)
        })

        fs.writeFileSync(`./demo_${themeName}_enhanced.svg`, outString)
        console.log(`✅ Generated enhanced demo for ${themeName} theme`)
    } catch (error) {
        console.log(`❌ Error generating ${themeName} theme:`, error.message)
    }
})

console.log("\n🎉 Enhanced demo SVGs generated successfully!")
console.log("Files created:")
themesToTest.forEach(themeName => {
    console.log(`  - demo_${themeName}_enhanced.svg`)
})
