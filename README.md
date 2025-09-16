# AstigmatismEasy Theme

A scientifically-optimized VS Code theme for developers with astigmatism and age-related vision decline. Available in **Night**, **Daylight**, and the new **Infrared** variant to support your entire coding workflow. The Night version is specifically designed for coding in low-light environments, especially beneficial for those wearing prismatic neuro lens glasses, the Daylight version provides enhanced visibility and comfort in brighter conditions, and the Infrared variant delivers an almost entirely red-shifted experience for ultra-low-light sessions.

> _Screenshot omitted to keep the repository free of binary assets required by some contribution workflows._

## 🌓 Theme Variants

AstigmatismEasy now comes in three variants to support your entire coding workflow:

### Night Theme
Optimized for low-light environments, the Night theme preserves dark adaptation and minimizes halation effects that are particularly problematic for developers with astigmatism when working in the dark. It uses the original deep contrast and color calibrations ideal for minimal ambient light.

### Infrared Theme (NEW)
Designed for extremely low ambient light (think planetarium, observatory, or red-room conditions), the Infrared theme keeps the entire UI—chrome, diagnostics, and syntax—within carefully tuned reds, corals, and peaches. Key characteristics include:
- Deeper oxblood background (`#140707`) with softened transparency to maintain OLED smoothness without producing hard edges.
- Rose-beige body text (`#F2D6C9`) and a full syntax palette of crimson, salmon, and peach hues that stay legible without injecting blue light.
- Diagnostics, terminal colors, and focus states recast in ember tones so the whole workspace remains red-shifted for long sessions without disrupting dark adaptation.

### Daylight Theme
The Daylight theme adapts the core scientific principles for use in rooms with more ambient light while remaining a dark theme. It features:
- Slightly lighter backgrounds for surrounding UI elements (like the Sidebar and Status Bar) for better visual separation from the editor in brighter conditions.
- Increased opacity and/or brightness for many secondary text elements (e.g., inactive line numbers, inlay hints, muted UI text) to improve their legibility against more ambient light.
- Maintained warm color palette and core editor syntax highlighting to reduce eye strain, even in brighter settings.
- Optimized overall UI contrast for readability without introducing glare, ensuring the theme remains comfortable for extended periods.

## 🔬 The Science Behind These Themes

This theme is based on extensive vision science research and addresses several key aspects of how astigmatism and other vision considerations affect coding:

### Low-Light Vision & Dark Adaptation

When working in dark environments, your eyes rely more on rod cells (scotopic vision) rather than cone cells. Rods are more sensitive to light but don't perceive color as well, and they undergo the Purkinje shift – becoming more sensitive to blue-green wavelengths as light dims. This is especially critical for the Night theme, but the principles of using warm colors and minimizing blue light benefit both variants by reducing overall eye strain.

**Our solution:**
- Uses predominantly warm colors (reds, oranges, yellows) for interface elements.
- Minimizes blue light that disrupts rhodopsin (the chemical responsible for night vision).
- Creates a balanced palette that preserves dark-adapted vision acuity (Night theme) and reduces general eye fatigue (both themes).

### Astigmatism, Contrast Sensitivity, and Glasses Wearers

Astigmatism causes light to focus unevenly, leading to blurred or ghosted vision. In dark conditions, pupils dilate, which can make astigmatic blur worse by highlighting corneal/lenticular imperfections. This often creates a "halation" effect where bright text on dark backgrounds blooms or halos. For developers wearing glasses, especially those with astigmatism or prismatic lenses, these effects can be compounded by glare, reflections off the lens surfaces, and chromatic aberration (color fringing).

**Our solution:**
- Uses a dark warm gray background (`#282828`) instead of pure black, and warm beige text (`#EBDBB2`) instead of stark white. This controlled, lower overall luminance reduces the intensity of light that can cause glare and reflections on glasses.
- Employs a warm color palette throughout, which can help minimize chromatic aberration (color fringing) that is sometimes more noticeable with certain lens coatings or prescriptions.
- Maintains optimal contrast ratios (typically 5:1 to 11:1) for all text elements, ensuring readability without excessive brightness that could exacerbate glare or halation.
- Avoids extreme contrast boundaries that worsen astigmatic haloing and can be particularly distracting when viewed through corrective lenses.

### Scientific Color Selection (Night & Daylight Editors)

Every color in these themes has been chosen based on vision science principles. The following table reflects the core syntax highlighting colors against the editor background, consistent across both Night and Daylight versions for the main coding area:

| Element  | Color   | Contrast (vs #282828) | Scientific Rationale                                                              |
|----------|---------|-----------------------|-----------------------------------------------------------------------------------|
| Background | #282828 | -                     | Dark enough for low luminance but not pure black to prevent halation/excessive glare |
| Text     | #EBDBB2 | 10.8:1                | Warm beige reduces blue component while maintaining readability                     |
| Keywords | #FB4934 | 7.5:1                 | Red has minimal impact on night vision while providing visual distinction           |
| Strings  | #8EC07C | 7.0:1                 | Green-teal is easier to focus than blue while remaining distinguishable           |
| Numbers  | #D3869B | 6.0:1                 | Desaturated purple provides contrast without excessive brightness                 |
| Comments | #BDAE93 | 6.3:1                 | Intentionally lower contrast for deemphasis while remaining legible & warm         |
### Infrared Variant Palette

The Infrared theme retains the same ergonomic philosophy while shifting every accent toward the red spectrum:

| Element  | Color   | Contrast (vs #140707) | Scientific Rationale |
|----------|---------|-----------------------|----------------------|
| Background | #140707 | - | Deep oxblood keeps luminance extremely low without going pitch black |
| Text     | #F2D6C9 | 14.3:1 | Rose-beige foreground keeps glyphs clear while avoiding blue components |
| Keywords | #FF6B6B | 7.1:1 | Crimson keywords provide emphasis without harsh saturation |
| Strings  | #FF9E80 | 9.8:1 | Salmon-peach strings preserve readability while staying in warm wavelengths |
| Numbers  | #F28CA5 | 8.5:1 | Dusty rose numerics separate literals without bright halos |
| Functions | #FFB4A2 | 11.6:1 | Peach-toned functions maintain hierarchy and strong contrast |
| Types    | #FF9780 | 9.4:1 | Coral types highlight structure while keeping the palette cohesive |
| Comments | #C69A92 | 7.9:1 | Muted clay comments stay legible yet comfortably subdued |


## ✨ Optimized for Mini LED & OLED at High Refresh Rates

This theme includes specific optimizations for developers using high-end displays:

### Mini LED Optimizations
- Careful color tuning to prevent blooming effect around bright UI elements.
- Subtle transparency adjustments for better edge transitions.
- Optimized contrast that takes advantage of Mini LED's excellent brightness control.

### OLED-Specific Enhancements
- Adjusted background transparency (`#282828FA` for editor in Night, `#282828F8` in Daylight) to prevent harsh edges with OLED's perfect blacks.
- Reduced saturation for bright UI elements to prevent "vibration" effect on high-contrast displays.
- Semi-transparent selection highlights to maintain visibility without causing eye strain.

### High Refresh Rate & Resolution Support
- Enhanced scrollbar visibility for easier tracking on 4K+ displays.
- Optimized terminal colors for high-resolution rendering.
- Subtle motion cues that take advantage of 120Hz+ refresh rates.

## 🐍 Language-Specific Enhancements

### Python
- Distinct highlighting for imports, built-ins, decorators, and magic methods.
- Special treatments for docstrings and format strings.
- Improved visual hierarchy for nested code structures.

### JavaScript/React/Next.js
- Enhanced component boundary visibility.
- Distinct styling for JSX tags, props, and expressions.
- Special handling for template literals and TypeScript types.

### Notebook Support
- Clear cell/output separation with background color differences.
- Improved status indicators for cell execution state.
- Complete syntax highlighting within notebook context.

## 🎨 Color Palette (Core)

The Night and Daylight themes use a carefully calibrated warm color palette for core syntax highlighting (the Infrared palette is detailed above):

- **Background**: `#282828` (very dark warm gray)
- **Text**: `#EBDBB2` (warm beige)
- **Comments**: `#BDAE93` (muted warm gray-brown)
- **Keywords**: `#FB4934` (soft red)
- **Operators**: `#FE8019` (orange)
- **Strings**: `#8EC07C` (soft aqua/green-teal)
- **Numbers**: `#D3869B` (dusty purple/mauve)
- **Types/Classes**: `#FABD2F` (golden yellow)
- **Functions**: `#B8BB26` (olive green)

*UI chrome elements in the Daylight theme use slightly adjusted background shades (e.g., `#32302F`) and opacities for better daytime visibility, while maintaining the overall warm aesthetic.*

## 📋 Installation

### VS Code

#### Via VS Code Marketplace

1.  Open VS Code
2.  Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
3.  Search for "AstigmatismEasy"
4.  Click Install
5.  Select your preferred theme variant:
    *   File > Preferences > Color Theme > **AstigmatismEasy Night**
    *   File > Preferences > Color Theme > **AstigmatismEasy Daylight**

#### Manual Installation

1.  Download or clone this repository.
2.  Copy the folder containing the theme JSON files to your VS Code extensions directory:
    *   Windows: `%USERPROFILE%\.vscode\extensions`
    *   macOS/Linux: `~/.vscode/extensions`
3.  Restart VS Code.
4.  Select your preferred theme variant:
    *   File > Preferences > Color Theme > **AstigmatismEasy Night**
    *   File > Preferences > Color Theme > **AstigmatismEasy Daylight**

### JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.)

The JetBrains version of AstigmatismEasy (currently available as a single "Night" optimized variant) is in active development and has been enhanced with additional innovations specifically designed to reduce halation and fringing for people with astigmatism:

- **OLED Display Optimizations**: Slightly transparent editor background and transparent gutter for smoother visuals.
- **Enhanced Structural Elements**: Braces, brackets, and parentheses with subtle background effects for better visibility.
- **Enhanced Keywords**: Keywords with subtle background effects to reduce contrast and halation.
- **Language-Specific Improvements**: Special treatments for Python, JavaScript/TypeScript, and Kotlin elements.

See the `INNOVATIONS.md` file (if applicable, e.g., in a `jetbrains-theme` subdirectory) for detailed information about these improvements and their scientific rationale.

#### Manual Installation

1.  Download the latest release of the JetBrains theme from the Releases page.
2.  Open your JetBrains IDE.
3.  Go to Settings/Preferences > Plugins.
4.  Click the gear icon and select "Install Plugin from Disk..."
5.  Navigate to the downloaded .jar file and select it.
6.  Restart the IDE when prompted.
7.  Go to Settings/Preferences > Appearance & Behavior > Appearance.
8.  Select "AstigmatismEasy" from the Theme dropdown.

#### Building from Source (JetBrains)

If you want to build the JetBrains theme plugin from source:
1. Clone this repository.
2. Navigate to the `jetbrains-theme` directory (or relevant directory).
3. Run the build script (e.g., `./build.sh`).
4. The plugin (e.g., `AstigmatismEasy-Theme-1.0.0.jar`) will be built.
5. Install the plugin using the Manual Installation instructions above.

## 🔧 Recommended Settings

### VS Code

For optimal experience with AstigmatismEasy in VS Code, consider these additional settings:

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

### JetBrains IDEs

The JetBrains version of AstigmatismEasy has been enhanced with comprehensive coverage of all IntelliJ UI components to ensure the theme is entirely consistent in following our coloring goals and reducing blue light exposure:

- **Comprehensive Warm Color Palette**: Every UI component uses warm colors to reduce blue light exposure.
- **Enhanced Eye Strain Prevention**: Carefully calibrated contrast ratios and color choices to minimize eye fatigue.
- **Blue Light Elimination**: Blue colors have been replaced with warmer alternatives throughout the entire interface.
- **Terminal Color Optimization**: ANSI blue replaced with muted brown/gray to reduce blue light in terminal output.
- **Consistent Syntax Highlighting**: Language-specific syntax highlighting that maintains the warm color palette.
- **Icon Color Optimization**: All icons use warm colors instead of blue to further reduce blue light exposure.

For optimal experience with AstigmatismEasy in JetBrains IDEs, consider these additional settings:

1.  **Font Settings** (Settings/Preferences > Editor > Font):
    *   Font: JetBrains Mono or Hack
    *   Size: 14
    *   Line height: 1.5
    *   Enable font ligatures: Disabled
2.  **Editor Settings** (Settings/Preferences > Editor > General):
    *   Caret blinking: No blinking
    *   Use block caret: Enabled
    *   Show whitespaces: Disabled (or as preferred)
3.  **Appearance Settings** (Settings/Preferences > Appearance & Behavior > Appearance):
    *   Animate windows: Disabled
    *   Smooth scrolling: Enabled
    *   Show navigation bar: Optional (disable for more space)
4.  **Anti-aliasing Settings** (Settings/Preferences > Editor > General > Appearance):
    *   Use anti-aliased font: Enabled
    *   Use subpixel anti-aliasing: (Consider 'Greyscale' or test what works best. Some find subpixel rendering distracting with astigmatism).
5.  **Additional Eye Strain Reduction** (Settings/Preferences > Appearance & Behavior > Appearance):
    *   Use custom font: Enabled (select a comfortable font)
    *   Override default fonts: Enabled
    *   Background image: Disabled (reduces visual noise)
    *   Adjust IDE font size when changing system font size: Enabled

## 🖥️ Display Recommendations

### For Mini LED Displays
- Set local dimming to Medium (not Maximum, to reduce blooming).
- Brightness:
    - **Night Theme**: 30-50% for dark environments.
    - **Daylight Theme**: Adjust as needed, typically 40-70% depending on ambient light.
- Contrast: Reduce to 80-90% of maximum.

### For OLED Displays
- Brightness:
    - **Night Theme**: 20-40% for dark environments.
    - **Daylight Theme**: Adjust as needed, typically 30-60% depending on ambient light.
- Enable pixel brightness limiter if available.

### For Both Display Types
- Color Temperature: 5000-5500K during day, 3000-4000K at night (if your display/OS supports it).
- Scaling: 125-150% recommended for 4K displays (or as comfortable).
- Enable motion blur reduction for high refresh rates if available and comfortable.

## 📚 References & Further Reading

This theme was created based on research from multiple scientific and community sources:

- Vision and contrast research from Bauer & Cavonius.
- Dark adaptation and red light studies from the National Park Service.
- Blue light and circadian rhythm research from CDC NIOSH.
- Astigmatism and halation studies from vision science journals.
- Community input from developers with astigmatism and vision challenges.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving this theme, especially from vision science or accessibility perspectives, please open an issue or submit a pull request.

## 📄 License

This theme is released under the MIT License.

---
