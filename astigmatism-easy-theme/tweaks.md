# AstigmatismEasy Theme Tweaks for JetBrains IDEs

This document outlines recommended tweaks and improvements for the AstigmatismEasy theme in JetBrains IDEs to better accommodate users with astigmatism and those wearing corrected lenses. These changes focus on reducing halation (light bleeding), improving contrast, and enhancing overall readability.

## Color Palette Refinements

The current color palette is well-chosen for reducing eye strain, but can be further optimized:

| Element | Current Color | Recommended Color | Rationale |
|---------|--------------|-------------------|-----------|
| Editor Background | `#282828` | `#282828F8` | Slight transparency helps with OLED displays, reducing pixel burn-in and softening harsh edges |
| Line Highlight | `#FE80191A` | `#FE801915` | Slightly reduced opacity to minimize distraction while maintaining focus |
| Selection Background | `#50494580` | `#50494575` | Slightly adjusted opacity for better text visibility within selections |
| Comments | `#BDAE93` | `#A89984` | Slightly darker to reduce visual noise while maintaining readability |
| Brackets/Braces | `#FE8019A0` | `#FE8019B0` | Increased opacity for better visibility of matching pairs |
| Error Highlighting | `#FB4934` (underline) | `#FB493470` (background) | Background highlighting is easier to see for people with astigmatism than underlines |

## Anti-Halation Improvements

Halation (light bleeding/fringing) is a common issue for people with astigmatism. These tweaks help reduce this effect:

1. **Reduce contrast between text and background**
   - Add a subtle text shadow to high-contrast elements:
   ```xml
   <option name="DEFAULT_KEYWORD">
     <value>
       <option name="FOREGROUND" value="#FB4934" />
       <option name="EFFECT_TYPE" value="4" /> <!-- Boxed effect -->
       <option name="EFFECT_COLOR" value="#FB493420" />
     </value>
   </option>
   ```

2. **Improve readability of brackets and parentheses**
   - Increase opacity and add subtle background:
   ```xml
   <option name="DEFAULT_BRACES">
     <value>
       <option name="FOREGROUND" value="#FE8019B0" />
       <option name="EFFECT_TYPE" value="4" />
       <option name="EFFECT_COLOR" value="#FE801920" />
     </value>
   </option>
   ```

3. **Optimize font rendering**
   - Add to IDE settings (not in theme files):
   ```
   Editor > Color Scheme > General > Text > Enable font ligatures: OFF
   Editor > Font > Enable antialiasing: ON
   Editor > Font > Enable subpixel rendering: OFF (for astigmatism)
   ```

## UI Element Improvements

### Editor

```json
"Editor": {
  "background": "#282828F8",
  "foreground": "#EBDBB2",
  "shortcutForeground": "#FE8019",
  "lineSeparatorColor": "#50494550",
  "selectionBackground": "#50494575",
  "selectionForeground": "#EBDBB2",
  "inactiveSelectionBackground": "#3C383675",
  "selectionInactiveBackground": "#3C383675",
  "searchResultsBackground": "#FABD2F30",
  "searchResultsBorderColor": "#FABD2F60",
  "foldedTextBackground": "#3C383640",
  "foldedTextBorderColor": "#50494550",
  "lineNumberColor": "#A8998480",
  "lineNumberColorSelected": "#FE8019",
  "tearLineColor": "#50494550",
  "currentLineBackground": "#FE801915",
  "rightMarginColor": "#50494550"
}
```

### Improved Indent Guides

Indent guides are crucial for code readability, especially for people with astigmatism:

```xml
<option name="INDENT_GUIDE" value="#50494560" />
<option name="VISUAL_INDENT_GUIDE" value="#50494560" />
<option name="SELECTED_INDENT_GUIDE" value="#FE801960" />
```

### Gutter and Line Numbers

Improved contrast for line numbers without being too bright:

```xml
<option name="LINE_NUMBERS_COLOR" value="#A8998490" />
<option name="LINE_NUMBER_ON_CARET_ROW_COLOR" value="#FE8019" />
<option name="GUTTER_BACKGROUND" value="#28282800" />
```

## Language-Specific Improvements

### Java/Kotlin

```xml
<option name="KOTLIN_FUNCTION_LITERAL_BRACES_AND_ARROW">
  <value>
    <option name="FOREGROUND" value="#FE8019B0" />
    <option name="FONT_TYPE" value="1" />
  </value>
</option>
<option name="KOTLIN_LABEL">
  <value>
    <option name="FOREGROUND" value="#FABD2F" />
    <option name="EFFECT_TYPE" value="4" />
    <option name="EFFECT_COLOR" value="#FABD2F20" />
  </value>
</option>
```

### JavaScript/TypeScript

```xml
<option name="JS.REGEXP">
  <value>
    <option name="FOREGROUND" value="#D3869B" />
    <option name="FONT_TYPE" value="2" />
    <option name="EFFECT_TYPE" value="4" />
    <option name="EFFECT_COLOR" value="#D3869B20" />
  </value>
</option>
```

### Python

```xml
<option name="PY.SELF_PARAMETER">
  <value>
    <option name="FOREGROUND" value="#FB4934" />
    <option name="FONT_TYPE" value="2" />
    <option name="EFFECT_TYPE" value="4" />
    <option name="EFFECT_COLOR" value="#FB493420" />
  </value>
</option>
```

## Additional UI Elements to Customize

### Improved Scrollbars

Scrollbars with better visibility but not distracting:

```json
"ScrollBar": {
  "Transparent": {
    "thumbColor": "#50494590",
    "thumbBorderColor": "#50494590",
    "hoverThumbColor": "#665c5490",
    "hoverThumbBorderColor": "#665c5490"
  },
  "thumbColor": "#50494590",
  "thumbBorderColor": "#50494590",
  "hoverThumbColor": "#665c5490",
  "hoverThumbBorderColor": "#665c5490",
  "trackColor": "#28282800",
  "trackBorderColor": "#28282800"
}
```

### Improved Tooltips and Documentation

```json
"ToolTip": {
  "background": "#3C3836F8",
  "foreground": "#EBDBB2",
  "borderColor": "#504945",
  "infoForeground": "#A89984",
  "Actions": {
    "background": "#3C3836F8",
    "infoForeground": "#A89984"
  }
}
```

### Improved Completion Popup

```json
"CompletionPopup": {
  "background": "#3C3836F8",
  "foreground": "#EBDBB2",
  "selectionBackground": "#504945",
  "selectionForeground": "#EBDBB2",
  "matchForeground": "#FE8019",
  "matchSelectionForeground": "#FE8019",
  "infoForeground": "#A89984",
  "descriptionForeground": "#A89984",
  "descriptionRightMargin": "#50494550"
}
```

## Font Recommendations

While not directly part of the theme files, font choice is crucial for astigmatism:

1. **Recommended Monospace Fonts:**
   - JetBrains Mono (with increased line height of 1.2)
   - Fira Code (with disabled ligatures)
   - Cascadia Code
   - IBM Plex Mono

2. **Font Settings:**
   - Size: 14-16px (larger than typical)
   - Line height: 1.2-1.3
   - Weight: Medium (not Light or Regular)
   - Anti-aliasing: Standard (not Greyscale)
   - Disable ligatures for clearer character distinction

## IDE Settings for Astigmatism

Additional IDE settings to complement the theme:

1. **Editor Settings:**
   - Enable "Show method separators" for better visual chunking
   - Set "Soft wrap" to ON for long lines
   - Increase "Right margin" to 100-120 characters
   - Set "Show whitespaces" to ON for trailing spaces only

2. **Appearance Settings:**
   - Disable animations where possible
   - Use "Compact" or "Medium" UI mode (not "Spacious")
   - Enable "Show editor breadcrumbs" for better navigation

## Terminal Improvements

Replace standard ANSI Blue with muted brown/gray to reduce blue light:

```xml
<option name="CONSOLE_BLUE_OUTPUT">
  <value>
    <option name="FOREGROUND" value="#BDAE93" />
  </value>
</option>
```

## Implementation Notes

To implement these changes:

1. Edit `AstigmatismEasy.xml` for editor color scheme changes
2. Edit `AstigmatismEasy.theme.json` for UI theme changes
3. Rebuild the theme plugin using the provided build script
4. Install the updated theme in your JetBrains IDE

## Scientific Rationale

These tweaks are based on vision science research related to astigmatism:

1. **Reduced Contrast:** High contrast can cause halation for astigmatic vision. Slightly reducing contrast while maintaining readability helps.

2. **Warm Color Palette:** Blue light is more prone to chromatic aberration in astigmatic vision. The warm palette reduces this effect.

3. **Subtle Backgrounds:** Background highlighting is easier to perceive than underlines for people with astigmatism.

4. **Increased Opacity for Structural Elements:** Making brackets and braces more visible helps with code structure comprehension.

5. **Reduced Transparency:** Semi-opaque UI elements can reduce the visual noise that affects astigmatic vision.
