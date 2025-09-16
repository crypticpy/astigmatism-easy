# AstigmatismEasy Theme

A scientifically-optimized VS Code theme for developers with astigmatism and age-related vision decline. Specifically designed for coding in low-light environments while wearing prismatic neuro lens glasses. Now available in Night, Daylight, and Infrared variants so you can stay comfortable across any lighting condition.

> _Screenshot omitted here so the repository stays free of binary assets._

## 🌒 Theme Variants

- **Night**: The original warm-dark experience tuned for minimizing halation while preserving contrast in very dim rooms.
- **Daylight**: Keeps the core editor colors but lightens supporting UI surfaces and increases opacity so the theme stays legible in brighter spaces.
- **Infrared**: A brand new, red-shifted palette with oxblood backgrounds, rose text, and ember diagnostics for astronomer-level dark adaptation.

## 🔬 The Science Behind This Theme

This theme is based on extensive vision science research and addresses several key aspects of how astigmatism affects coding in dark environments:

### Low-Light Vision & Dark Adaptation

When working in dark environments, your eyes rely more on rod cells (scotopic vision) rather than cone cells. Rods are more sensitive to light but don't perceive color as well, and they undergo the Purkinje shift – becoming more sensitive to blue-green wavelengths as light dims.

**Our solution:**
- Uses predominantly warm colors (reds, oranges, yellows) for interface elements
- Minimizes blue light that disrupts rhodopsin (the chemical responsible for night vision)
- Creates a balanced palette that preserves dark-adapted vision acuity

### Astigmatism and Contrast Sensitivity

Astigmatism causes light to focus unevenly, leading to blurred or ghosted vision. In dark conditions, pupils dilate, which makes astigmatic blur worse – highlighting corneal/lenticular imperfections. This creates a "halation" effect where bright text on dark backgrounds blooms or halos.

**Our solution:**
- Uses a dark warm gray background (#282828) instead of pure black
- Implements warm beige text (#EBDBB2) instead of stark white
- Maintains optimal contrast ratios (5:1 to 11:1) for all text elements
- Avoids extreme contrast boundaries that worsen astigmatic haloing

### Scientific Color Selection

Every color in the Night and Daylight variants has been chosen based on vision science principles:

| Element | Color | Contrast | Scientific Rationale |
|---------|-------|----------|---------------------|
| Background | #282828 | - | Dark enough for low luminance but not pure black to prevent halation |
| Text | #EBDBB2 | 10.8:1 | Warm beige reduces blue component while maintaining readability |
| Keywords | #FB4934 | 7.5:1 | Red has minimal impact on night vision while providing visual distinction |
| Strings | #8EC07C | 7.0:1 | Green-teal is easier to focus than blue while remaining distinguishable |
| Numbers | #D3869B | 6.0:1 | Desaturated purple provides contrast without excessive brightness |
| Comments | #A89984 | 5.3:1 | Intentionally lower contrast for deemphasis while remaining legible |

**Infrared Variant Palette**

The Infrared theme keeps the same ergonomic goals while shifting every interface element toward red hues:

| Element | Color | Contrast | Scientific Rationale |
|---------|-------|----------|---------------------|
| Background | #140707 | - | Deep oxblood keeps luminance extremely low without using pure black |
| Text | #F2D6C9 | 14.3:1 | Rose-beige text maintains clarity while removing blue wavelengths |
| Keywords | #FF6B6B | 7.1:1 | Crimson keywords provide emphasis without harsh saturation |
| Strings | #FF9E80 | 9.8:1 | Salmon tones stay legible and soothing during long sessions |
| Numbers | #F28CA5 | 8.5:1 | Dusty rose numerics separate data without blooming |
| Comments | #C69A92 | 7.9:1 | Muted clay comments remain readable yet understated |

## ✨ Optimized for Mini LED & OLED at High Refresh Rates

This theme includes specific optimizations for developers using high-end displays:

### Mini LED Optimizations
- Careful color tuning to prevent blooming effect around bright UI elements
- Subtle transparency adjustments for better edge transitions
- Optimized contrast that takes advantage of Mini LED's excellent brightness control

### OLED-Specific Enhancements
- Adjusted background transparency (`#282828FA`) to prevent harsh edges with OLED's perfect blacks
- Reduced saturation for bright UI elements to prevent "vibration" effect on high-contrast displays
- Semi-transparent selection highlights to maintain visibility without causing eye strain

### High Refresh Rate & Resolution Support
- Enhanced scrollbar visibility for easier tracking on 4K+ displays
- Optimized terminal colors for high-resolution rendering
- Subtle motion cues that take advantage of 120Hz+ refresh rates

## 🐍 Language-Specific Enhancements

### Python
- Distinct highlighting for imports, built-ins, decorators, and magic methods
- Special treatments for docstrings and format strings
- Improved visual hierarchy for nested code structures

### JavaScript/React/Next.js
- Enhanced component boundary visibility
- Distinct styling for JSX tags, props, and expressions
- Special handling for template literals and TypeScript types

### Notebook Support
- Clear cell/output separation with background color differences
- Improved status indicators for cell execution state
- Complete syntax highlighting within notebook context

## 🎨 Color Palette

The Night and Daylight variants use a carefully calibrated warm color palette:

- **Background**: #282828 (very dark warm gray)
- **Text**: #EBDBB2 (warm beige)
- **Comments**: #A89984 (muted gray-brown)
- **Keywords**: #FB4934 (soft red)
- **Operators**: #FE8019 (orange)
- **Strings**: #8EC07C (soft aqua/green-teal)
- **Numbers**: #D3869B (dusty purple/mauve)
- **Types/Classes**: #FABD2F (golden yellow)
- **Functions**: #B8BB26 (olive green)

**Infrared variant highlights:**

- **Background**: #140707 (deep oxblood)
- **Text**: #F2D6C9 (rose beige)
- **Comments**: #C69A92 (muted clay)
- **Keywords**: #FF6B6B (crimson)
- **Operators**: #FF7F6E (ember)
- **Strings**: #FF9E80 (salmon-peach)
- **Numbers**: #F28CA5 (dusty rose)
- **Types/Classes**: #FF9780 (coral)
- **Functions**: #FFB4A2 (peach)

## 📋 Installation

### Via VS Code Marketplace

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "AstigmatismEasy"
4. Click Install

### Manual Installation

1. Download or clone this repository
2. Copy the folder to your VS Code extensions directory:
   - Windows: `%USERPROFILE%\.vscode\extensions`
   - macOS/Linux: `~/.vscode/extensions`
3. Restart VS Code
4. Select the theme: File > Preferences > Color Theme > AstigmatismEasy

## 🔧 Recommended Settings

For optimal experience with AstigmatismEasy, consider these additional VS Code settings:

```json
{
  "editor.fontSize": 14,
  "editor.lineHeight": 1.5,
  "editor.letterSpacing": 0.5,
  "editor.fontFamily": "'JetBrains Mono', 'Hack', Consolas, monospace",
  "editor.fontLigatures": false,
  "editor.cursorBlinking": "solid",
  "editor.cursorWidth": 2,
  "editor.minimap.enabled": false,
  "workbench.list.smoothScrolling": true,
  "editor.smoothScrolling": true,
  "terminal.integrated.smoothScrolling": true
}
```

## 🖥️ Display Recommendations

### For Mini LED Displays
- Set local dimming to Medium (not Maximum)
- Brightness: 40-60% for dark environments
- Contrast: Reduce to 80-90% of maximum

### For OLED Displays
- Brightness: 30-50% for dark environments
- Enable pixel brightness limiter if available

### For Both Display Types
- Color Temperature: 5000-5500K during day, 3000-4000K at night
- Scaling: 125-150% recommended for 4K displays
- Enable motion blur reduction for high refresh rates

## 📚 References & Further Reading

This theme was created based on research from multiple scientific and community sources:

- Vision and contrast research from Bauer & Cavonius
- Dark adaptation and red light studies from the National Park Service
- Blue light and circadian rhythm research from CDC NIOSH
- Astigmatism and halation studies from vision science journals
- Community input from developers with astigmatism and vision challenges

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving this theme, especially from vision science or accessibility perspectives, please open an issue or submit a pull request.

## 📄 License

This theme is released under the MIT License.
