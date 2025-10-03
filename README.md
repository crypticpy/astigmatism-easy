# AstigmatismEasy Theme

A scientifically-optimized suite of VS Code themes for developers with astigmatism, neuro-lens corrections, and age-related vision decline. AstigmatismEasy now includes multiple physiologically informed color families and adaptive luminance profiles so you can match both ambient lighting and display technology without sacrificing eye comfort.

![AstigmatismEasy Night Theme Preview](https://github.com/yourusername/astigmatism-easy/raw/main/images/night-theme-preview.png)
*Replace with actual Night theme preview image and correct path*

![AstigmatismEasy Daylight Theme Preview](https://github.com/yourusername/astigmatism-easy/raw/main/images/daylight-theme-preview.png)
*Replace with actual Daylight theme preview image and correct path*

## 🌓 Theme Families & Adaptive Profiles

The theme collection now ships with six scientifically curated families, each tuned for a specific visual scenario. Infrared, Night, and Daylight also include adaptive luminance profiles so you can fine-tune contrast without manually editing JSON files.

- **Night — Halation Guard**: Refined version of the original warm palette. Soft micro-textured chrome, halo-controlled highlights, and tuned diagnostics for pure dark environments and OLED panels.
- **Daylight — Harmonic Ambient**: Brighter UI shells and increased secondary text luminance to remain legible in mixed or brighter rooms while retaining the low-blue baseline of the night palette.
- **Infrared — Deep‑IR / Scotopic Calm / Mesopic Focus / Photopic Clarity**: Red-spectrum variants designed for late-night workflows. Pick Scotopic for maximal dark adaptation, Mesopic for evening ambient light, or Photopic when switching under brighter conditions without leaving the warm infrared colorway.
- **Purkinje Violet — Twilight Contrast**: Violet-rose hues anchored to the Purkinje shift for twilight hours, offering additional chroma variety without introducing blue glare.
- **Mesopic Moss — Ambient Balance**: Green/olive family tuned for day-to-dusk transitions, balancing rod and cone stimulation to reduce accommodative stress in variable lighting.
- **Photopic Ember — High-Ambient Comfort**: Amber/orange spectrum optimized for high-luminance workspaces and crisp mini-LED displays where glare control is critical.

Each profile keeps ΔL* spacing within 6–8 between major UI planes to avoid bloom, and terminal/editor separations are intentionally larger so context switching remains effortless. Reload the theme after installing to see all variants in the command palette.

## 🔬 The Science Behind These Themes

This theme is based on extensive vision science research and addresses several key aspects of how astigmatism and other vision considerations affect coding:

### Low-Light Vision & Dark Adaptation

When working in dark environments, your eyes rely more on rod cells (scotopic vision) rather than cone cells. Rods are more sensitive to light but don't perceive color as well, and they undergo the Purkinje shift – becoming more sensitive to blue-green wavelengths as light dims. This is especially critical for the Halation Guard and Infrared profiles, but the principles of using warm colors and minimizing blue light benefit every variant by reducing overall eye strain.

**Our solution:**
- Uses predominantly warm colors (reds, oranges, yellows) for interface elements across the family.
- Minimizes blue light that disrupts rhodopsin (the chemical responsible for night vision).
- Creates a balanced palette that preserves dark-adapted vision acuity in night-oriented profiles while reducing general eye fatigue in brighter variants.

### Astigmatism, Contrast Sensitivity, and Glasses Wearers

Astigmatism causes light to focus unevenly, leading to blurred or ghosted vision. In dark conditions, pupils dilate, which can make astigmatic blur worse by highlighting corneal/lenticular imperfections. This often creates a "halation" effect where bright text on dark backgrounds blooms or halos. For developers wearing glasses, especially those with astigmatism or prismatic lenses, these effects can be compounded by glare, reflections off the lens surfaces, and chromatic aberration (color fringing).

**Our solution:**
- Uses a dark warm gray background (`#282828`) instead of pure black, and warm beige text (`#EBDBB2`) instead of stark white. This controlled, lower overall luminance reduces the intensity of light that can cause glare and reflections on glasses.
- Employs a warm color palette throughout, which can help minimize chromatic aberration (color fringing) that is sometimes more noticeable with certain lens coatings or prescriptions.
- Maintains optimal contrast ratios (typically 5:1 to 11:1) for all text elements, ensuring readability without excessive brightness that could exacerbate glare or halation.
- Avoids extreme contrast boundaries that worsen astigmatic haloing and can be particularly distracting when viewed through corrective lenses.

### Scientific Color Selection (Core Editor)

Every color in this suite has been chosen based on vision science principles. The following table reflects the base syntax palette used by the Halation Guard profile; other families shift hue and luminance while preserving the same contrast goals:

| Element  | Color   | Contrast (vs #282828) | Scientific Rationale                                                              |
|----------|---------|-----------------------|-----------------------------------------------------------------------------------|
| Background | #282828 | -                     | Dark enough for low luminance but not pure black to prevent halation/excessive glare |
| Text     | #EBDBB2 | 10.8:1                | Warm beige reduces blue component while maintaining readability                     |
| Keywords | #FB4934 | 7.5:1                 | Red has minimal impact on night vision while providing visual distinction           |
| Strings  | #8EC07C | 7.0:1                 | Green-teal is easier to focus than blue while remaining distinguishable           |
| Numbers  | #D3869B | 6.0:1                 | Desaturated purple provides contrast without excessive brightness                 |
| Comments | #BDAE93 | 6.3:1                 | Intentionally lower contrast for deemphasis while remaining legible & warm         |

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

The theme uses a carefully calibrated warm color palette for core syntax highlighting:

- **Background**: `#282828` (very dark warm gray)
- **Text**: `#EBDBB2` (warm beige)
- **Comments**: `#BDAE93` (muted warm gray-brown)
- **Keywords**: `#FB4934` (soft red)
- **Operators**: `#FE8019` (orange)
- **Strings**: `#8EC07C` (soft aqua/green-teal)
- **Numbers**: `#D3869B` (dusty purple/mauve)
- **Types/Classes**: `#FABD2F` (golden yellow)
- **Functions**: `#B8BB26` (olive green)

*UI chrome elements in the Daylight, Mesopic Moss, and Photopic Ember themes use slightly brighter background shades while Purkinje Violet and Infrared profiles employ deeper overlays to limit bloom, all while maintaining the warm aesthetic.*

## 🧰 Adaptive Tooling & Utilities

- **Profile generator**: The repository includes `tools/build_theme_variants.py`, which rebuilds every variant and adaptive profile from the Infrared baseline. Run it after tweaking palettes to keep all JSON files in sync.
- **Temporal comfort pack**: `extras/infrared-temporal-settings.json` bundles cursor, scrolling, and font metrics tuned for Neurolens and high-refresh displays. Drop it into your `settings.json` and adjust as needed per profile.
- **Contrast audit**: `tools/contrast_report.py` measures WCAG-style contrast ratios and ΔL* spacings for editor/terminal pairs to verify that customizations stay within our 5:1–11:1 target window.
- **Ambient switching**: Each family appears in the VS Code theme picker (e.g., “AstigmatismEasy Infrared — Mesopic Focus”). Switch variants as ambient light changes rather than altering display brightness mid-session.

## 📋 Installation

### VS Code

#### Via VS Code Marketplace

1.  Open VS Code
2.  Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
3.  Search for "AstigmatismEasy"
4.  Click Install
5.  Select your preferred theme variant:
    *   File > Preferences > Color Theme > **AstigmatismEasy Night — Halation Guard**
    *   …or switch among **Infrared (Scotopic/Mesopic/Photopic)**, **Daylight — Harmonic Ambient**, **Purkinje Violet — Twilight Contrast**, **Mesopic Moss — Ambient Balance**, and **Photopic Ember — High-Ambient Comfort** depending on your environment.

#### Manual Installation

1.  Download or clone this repository.
2.  Copy the folder containing the theme JSON files to your VS Code extensions directory:
    *   Windows: `%USERPROFILE%\.vscode\extensions`
    *   macOS/Linux: `~/.vscode/extensions`
3.  Restart VS Code.
4.  Select your preferred theme variant from the command palette (same names as above).

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

For a plug-and-play preset aligned with the Infrared profiles, import the `extras/infrared-temporal-settings.json` file and then layer any project-specific overrides on top.

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