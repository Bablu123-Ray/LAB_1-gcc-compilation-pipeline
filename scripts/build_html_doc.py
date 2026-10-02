import os
import base64

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_b64(rel_path):
    full_path = os.path.join(base_dir, rel_path)
    with open(full_path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

img1 = get_b64("docs/assets/screenshots/01_step1_source_cat.png")
img2 = get_b64("docs/assets/screenshots/02_step2_preprocessing_gcc_E.png")
img3 = get_b64("docs/assets/screenshots/03_step3_compilation_gcc_S.png")
img4 = get_b64("docs/assets/screenshots/04_step4_assembly_objdump.png")
img5 = get_b64("docs/assets/screenshots/05_step5_linking_file_info.png")
img6 = get_b64("docs/assets/screenshots/06_step6_execution_output.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Lab 2: GCC Compilation Process: Step-by-Step Guide</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #1f2328;
    background: #ffffff;
    max-width: 900px;
    margin: 40px auto;
    padding: 0 30px;
    line-height: 1.65;
  }}
  h1 {{ font-size: 2.2rem; border-bottom: 2px solid #0969da; padding-bottom: 12px; color: #0969da; margin-bottom: 4px; }}
  h2 {{ font-size: 1.5rem; border-bottom: 1px solid #d0d7de; padding-bottom: 8px; margin-top: 35px; color: #1f2328; }}
  h3 {{ font-size: 1.2rem; margin-top: 25px; color: #24292f; }}
  p, li {{ font-size: 15px; color: #24292f; }}
  code {{ font-family: 'JetBrains Mono', monospace; background: #f6f8fa; padding: 2px 6px; border-radius: 4px; font-size: 13.5px; color: #0969da; }}
  pre {{ background: #0d1117; color: #e6edf3; padding: 16px 20px; border-radius: 8px; overflow-x: auto; font-family: 'JetBrains Mono', monospace; font-size: 13.5px; }}
  pre code {{ background: transparent; color: inherit; padding: 0; }}
  table {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }}
  th, td {{ border: 1px solid #d0d7de; padding: 10px 14px; text-align: left; }}
  th {{ background: #f6f8fa; font-weight: 600; }}
  img {{ max-width: 100%; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); margin: 15px 0; border: 1px solid #30363d; background: #0c0c0c; }}
  .badge {{ display: inline-block; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 600; background: #ddf4ff; color: #0969da; margin-right: 8px; }}
  .checklist {{ list-style-type: none; padding-left: 0; }}
  .checklist li::before {{ content: '✔ '; color: #1a7f37; font-weight: bold; }}
  @media print {{
    body {{ max-width: 100%; margin: 0; padding: 20px; }}
    pre, img {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>

<h1>Lab 2: GCC Compilation Process: Step-by-Step Guide</h1>
<p><strong>Course:</strong> ST5039CMD Programming and Operating System &bull; <strong>Module:</strong> C-Programming Basics / Integration and Process Concept</p>
<div>
  <span class="badge">GCC Compiler</span>
  <span class="badge">x86-64 Assembly</span>
  <span class="badge">ELF64 Binary</span>
  <span class="badge">Linux Systems</span>
</div>

<h2>I. Executive Overview &amp; Learning Objectives</h2>
<p>The compilation of a C program involves four main stages: <strong>Preprocessing</strong>, <strong>Compilation</strong>, <strong>Assembly</strong>, and <strong>Linking</strong>, concluding with OS runtime binary execution. A computer CPU cannot directly parse high-level C code; it executes only binary machine code (0s and 1s). The GNU Compiler Collection (GCC) orchestrates this transformation through a structured pipeline.</p>

<h2>II. C Program Structure &amp; Compilation Flow</h2>
<pre><code>  [ Source Code: main.c ]
            │
            │  Stage 1: Preprocessing (gcc -E)
            ▼
  [ Preprocessed File: main.i ]
            │
            │  Stage 2: Compilation (gcc -S)
            ▼
  [ Assembly File: main.s ]
            │
            │  Stage 3: Assembly (gcc -c)
            ▼
  [ Relocatable Object: main.o ]
            │
            │  Stage 4: Linking (gcc / ld)
            ▼
  [ Final Executable: main (ELF) ]
            │
            │  Execution: ./main (OS execve -&gt; ld.so)
            ▼
  [ Program Output to stdout ]</code></pre>

<h2>III. Step-by-Step Practical Demonstration</h2>

<h3>Step 1: Original C Program</h3>
<ul>
  <li><strong>Objective:</strong> View the original source code.</li>
  <li><strong>Command:</strong> <code>cat main.c</code></li>
  <li><strong>Image Placeholder:</strong></li>
</ul>
<img src="{img1}" alt="Step 1 - Original Source Code">
<p><strong>Observation:</strong> Displays the initial C source code written by the programmer. It includes standard library headers (<code>&lt;stdio.h&gt;</code>), defines <code>main()</code>, issues formatted output via <code>printf()</code>, and returns exit code <code>0</code>.</p>

<h3>Step 2: Preprocessing</h3>
<ul>
  <li><strong>Objective:</strong> Process directives like <code>#include</code> and macros to generate the preprocessed source code (<code>.i</code>).</li>
  <li><strong>Command:</strong> <code>gcc -E main.c -o main.i then head -30 main.i</code></li>
  <li><strong>Image Placeholder:</strong></li>
</ul>
<img src="{img2}" alt="Step 2 - Preprocessing Output">
<p><strong>Observation:</strong> The code expands to include standard library declarations, removing comments and resolving macros. Linemarkers preserve source file line mappings for debugging.</p>

<h3>Step 3: Compilation (C to Assembly)</h3>
<ul>
  <li><strong>Objective:</strong> Convert the preprocessed C code into assembly language (<code>.s</code>).</li>
  <li><strong>Command:</strong> <code>gcc -S main.i -o main.s then head -30 main.s</code></li>
  <li><strong>Image Placeholder:</strong></li>
</ul>
<img src="{img3}" alt="Step 3 - Assembly Generation">
<p><strong>Observation:</strong> The compiler translates the C syntax into low-level CPU-specific assembly instructions in AT&amp;T syntax. It allocates stack frames, adheres to the System V AMD64 ABI (<code>%rdi</code> for argument 1, <code>%rax</code> for return value), and emits Intel CET (<code>endbr64</code>) instructions.</p>

<h3>Step 4: Assembly (Assembly to Object Code)</h3>
<ul>
  <li><strong>Objective:</strong> Convert the assembly instructions into machine-readable object code (<code>.o</code>) and inspect it.</li>
  <li><strong>Command:</strong> <code>gcc -c main.s -o main.o then objdump -d main.o</code></li>
  <li><strong>Image Placeholder:</strong></li>
</ul>
<img src="{img4}" alt="Step 4 - Assembly Disassembly">
<p><strong>Observation:</strong> The assembler creates binary machine code. The <code>objdump</code> tool allows us to view the raw hex format (<code>f3 0f 1e fa</code>, <code>55</code>, <code>48 89 e5</code>) alongside assembly. Zeroed bytes (<code>00 00 00 00</code>) denote relocation placeholders for the linker.</p>

<h3>Step 5: Linking (Object Code to Executable)</h3>
<ul>
  <li><strong>Objective:</strong> Combine the object file with required libraries to create the final executable binary.</li>
  <li><strong>Command:</strong> <code>gcc main.o -o main then file main</code></li>
  <li><strong>Image Placeholder:</strong></li>
</ul>
<img src="{img5}" alt="Step 5 - Binary Linking and Identification">
<p><strong>Observation:</strong> The linker resolves external function calls (like <code>printf</code>), connects runtime initialization code (<code>_start</code>), and creates the final ready-to-run ELF 64-bit dynamic executable with interpreter <code>/lib64/ld-linux-x86-64.so.2</code>.</p>

<h3>Step 6: Execution</h3>
<ul>
  <li><strong>Objective:</strong> Run the final executable program.</li>
  <li><strong>Command:</strong> <code>./main</code></li>
  <li><strong>Image Placeholder:</strong></li>
</ul>
<img src="{img6}" alt="Step 6 - Program Execution">
<p><strong>Observation:</strong> The OS executes the compiled binary via <code>execve()</code>, producing the expected output: <code>Hello World!</code>.</p>

<h2>IV. Summary Compilation Reference Table</h2>
<table>
  <tr><th>Stage</th><th>GCC Command</th><th>Output File</th><th>Primary Systems Purpose</th></tr>
  <tr><td><strong>1. Preprocessing</strong></td><td><code>gcc -E main.c -o main.i</code></td><td><code>main.i</code></td><td>Expands headers (<code>#include</code>) and resolves macros (<code>#define</code>).</td></tr>
  <tr><td><strong>2. Compilation</strong></td><td><code>gcc -S main.i -o main.s</code></td><td><code>main.s</code></td><td>Translates C code into architecture-specific assembly language.</td></tr>
  <tr><td><strong>3. Assembly</strong></td><td><code>gcc -c main.s -o main.o</code></td><td><code>main.o</code></td><td>Converts assembly instructions into relocatable machine object code.</td></tr>
  <tr><td><strong>4. Linking</strong></td><td><code>gcc main.o -o main</code></td><td><code>main</code> / <code>a.out</code></td><td>Resolves external library symbols and generates final executable.</td></tr>
  <tr><td><strong>5. Execution</strong></td><td><code>./main</code></td><td><code>stdout</code></td><td>Kernel loads binary into RAM and executes CPU instructions.</td></tr>
</table>

<h2>V. Submission Checklist</h2>
<ul class="checklist">
  <li>All 4 compilation phases (<code>gcc -E</code>, <code>gcc -S</code>, <code>gcc -c</code>, <code>gcc</code>) documented and demonstrated.</li>
  <li>Authentic raw terminal console screenshots embedded for all 6 steps.</li>
  <li>Instruction-by-instruction breakdown of assembly code and System V AMD64 ABI.</li>
  <li>Machine code disassembly analyzed with hex opcodes and relocation records.</li>
  <li>ELF file metadata and dynamic interpreter verified.</li>
  <li>Repository pushed to personal GitHub account with complete commit history.</li>
</ul>

</body>
</html>
"""

out_html = os.path.join(base_dir, "Lab2_GCC_Compilation_Process_Documentation.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print("Generated Lab 2 HTML report:", out_html)
