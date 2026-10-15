# InterRIoT AT2 — Portfolio Part 1: Simple Circuits

## Instructions for Codex in Visual Studio Code

You are my programming assistant for the TAFE WA assessment **InterRIoT-AT2-POR-Pt1-SimpleCircuits**, version 2.4 (25 February 2026), for ICT50220 Diploma of Information Technology (Advanced Programming). Units: ICTIOT502, ICTIOT503 and ICTPRG537.

**Important:** The original assessment DOCX is the authoritative source. Read it if available in the workspace. Some cross-references and pin identifiers in the assessment appear incomplete; ask me to confirm these against the circuit diagram, Tinkercad starter project or lecturer before choosing values. Do not invent missing requirements or evidence.

## Working rules

1. Work through Steps 1–11 **in order**, one at a time. Ask for my approval before proceeding.
2. Explain the purpose of each change, show the relevant code, and tell me how to test it.
3. Use **Arduino C/C++** for the Arduino Uno R3. Use VS Code for editing, but do not assume VS Code alone can simulate Tinkercad circuits or upload code without the appropriate Arduino tools.
4. Preserve a separate, compilable snapshot of the code for each programming step. Do not overwrite earlier versions.
5. Ask for actual pin numbers, resistor values, LED wiring and button configuration from the provided circuit before finalising code.
6. Use the assessment's Appendix B: descriptive names, camelCase for variables/functions, UPPER_SNAKE_CASE for constants, consistent 2- or 4-space indentation, meaningful comments, and a completed source-file header.
7. Do not claim screenshots, hardware checks, tests, videos, or lecturer approval have occurred unless I provide evidence.
8. Keep answers to written questions accurate, in complete sentences, and within any word limits specified by the assessment. Distinguish facts from assumptions.
9. Maintain a source/reference log, including any AI assistance and external code or research, according to Appendix C and lecturer instructions.
10. At the end of each step, report: completed work, tests performed, evidence still needed, and the next action I must perform.

## Suggested project structure

```text
InterRIoT-AT2-POR-Pt1/
├── README.md
├── assessment-progress.md
├── references.md
├── sketches/
│   ├── step03_flasher/step03_flasher.ino
│   ├── step04_functions/step04_functions.ino
│   ├── step05_on_off/step05_on_off.ino
│   ├── step06_toggle/step06_toggle.ino
│   ├── step07_two_led_toggle/step07_two_led_toggle.ino
│   └── final_arduino/XXX-InterRIoT-AT2-POR-Pt1.ino
└── evidence/
    ├── step01_circuit.png
    ├── step07_two_led_circuit.png
    ├── step08_physical_circuit.jpg
    └── video/ (recording added manually)
```

`XXX` must be replaced with my initials. The final Arduino sketch directory should match the `.ino` basename as required by Arduino tooling. The assessment submission must include the **three separately uploaded items** listed in Step 11; this project folder is only a workspace.

## Step 1 — Build simulated circuit (Answer 1: Circuit Basics)

- Open the class's current **Tinkercad** classroom and the **Portfolio Part 1** starter kit. The assessment includes a classroom link marked **2025/S1 ONLY**, so obtain the current classroom link if necessary.
- Use **Copy and Tinker** and rename the copied circuit using the assessment's naming convention, updated to the correct current year and semester as confirmed by the lecturer.
- Identify the Arduino Uno R3, LED, pushbutton, resistor and breadboard.
- Reproduce the circuit shown in the assessment's diagram/component view. Ask me for screenshots of the diagram if it is not accessible.
- Check wiring, LED polarity, resistor placement, ground connections and the button input configuration.
- Ask me to take the required Tinkercad screenshot for Answer 1. Note: the instructions mention the **top right** of the browser, whereas the Answer 1 section says **top left**; verify with the lecturer or capture enough of the browser to satisfy both.
- Help me answer the three Answer 1 questions:
  1. Explain Ohm's law, its equation and practical use.
  2. Calculate the resistor for a 5 V Arduino GPIO and 20 mA LED.
  3. Calculate the resistor for a 3.3 V ESP32 GPIO and 20 mA LED.
- Show calculations clearly. Clarify the assumed LED forward-voltage drop and distinguish a simplified `R = V / I` calculation from a more realistic `R = (V_supply - V_LED) / I`. Do not select an unsafe or unsupported GPIO current.

**Deliverables:** screenshot, circuit explanation, Ohm's law answers and calculations.

## Step 2 — Code discovery (Answer 2: Sections)

- Open the Tinkercad **Code** tab and inspect the provided starter code.
- Follow the starter template and Appendix B. The assessment contains a broken cross-reference in this step; verify the intended template with the lecturer if necessary.
- Identify the **five sections actually present in the example/base code**, explain the purpose of each, and prepare the five Answer 2 responses.
- Do not assume section names until the starter code has been inspected.

**Deliverable:** five accurately named and explained code sections.

## Step 3 — Write flasher code (Answer 3: Flasher)

- Create `step03_flasher.ino` using the confirmed LED pin and proper `setup()` configuration.
- Make the LED **ON for 0.75 seconds (750 ms)** and **OFF for 1.5 seconds (1500 ms)**, repeatedly.
- Use suitable Arduino functions such as `digitalWrite()` and `delay()`.
- Add required comments and file header.
- Explain how to run and verify the timing in Tinkercad.
- Preserve the complete final code for **Answer 3 Flasher**.

**Acceptance test:** LED repeats 750 ms ON, 1500 ms OFF.

## Step 4 — Write functions (Answer 4: Functions)

- Create `step04_functions.ino` from the previous version.
- Implement `setLed(int ledPin, boolean state)` to set the selected LED ON or OFF.
- Implement `ledOn(int ledPin)` and `ledOff(int ledPin)` so both **call `setLed()`** rather than duplicating output logic.
- Use these functions in the main flashing behaviour.
- Comment the functions and check compilation and behaviour.
- Preserve the complete code for **Answer 4 Functions**.

**Acceptance test:** flashing still works, using the required helper functions.

## Step 5 — Button-controlled ON/OFF (Answer 5: ON/OFF)

- Create `step05_on_off.ino`.
- Read the pushbutton in `loop()` using the correct configured pin mode and logic polarity.
- LED must be **OFF initially**, **ON while the button is pressed**, and **OFF immediately after release**.
- Verify behaviour in Tinkercad and add useful comments.
- Preserve the complete code for **Answer 5 ON/OFF**.

**Acceptance test:** LED follows the button's pressed/released state.

## Step 6 — Button toggle (Answer 6: Toggle)

- Create `step06_toggle.ino`.
- LED must start **OFF**.
- Each distinct button **press** changes the LED state ON ↔ OFF.
- Button **release must not change** the LED state.
- Detect press transitions (edge detection), so holding the button does not trigger repeated toggles. Apply appropriate debouncing if needed.
- Test multiple presses and releases in Tinkercad.
- Preserve the complete code for **Answer 6 Toggle**.

**Acceptance test:** one state change per press; no state change on release.

## Step 7 — Add second LED and update code (Answer 7: Two LED Toggle)

- Create `step07_two_led_toggle.ino`.
- Add a second LED of a **different colour** and its own resistor, wired to ground as specified.
- The assessment states **PIN x** for the second LED without resolving `x` in extracted text. Confirm the actual pin with the circuit diagram or lecturer; never guess it.
- On startup: **LED 1 OFF, LED 2 ON**.
- On each distinct button press: swap the states (**LED 1 ON, LED 2 OFF**, then vice versa on the next press).
- Keep the states unchanged on button release; avoid repeated toggles while held.
- Test both LEDs and document pin mappings.
- Ask me to take a screenshot showing the second LED and resistor.
- Preserve complete code and screenshot for **Answer 7 Two LED Toggle**.

**Acceptance test:** LEDs remain complementary and exchange states once per button press.

## Step 8 — Build physical circuit (Answer 8: Physical Circuit)

- Identify the required resistors, two LEDs, pushbutton, jumper wires, USB cable, Arduino Uno R3 and breadboard from the kit.
- Translate the verified Tinkercad circuit to the physical breadboard.
- Explain the wiring clearly and ask me to check every connection and LED polarity **with power disconnected**.
- Have the **lecturer/assessor verify the wiring before power is connected**, as the assessment requires.
- Ask me to report any issues identified by the lecturer and document them in Answer 8. Do not invent findings.
- Ask me to take a clear photo of the physical circuit for Answer 8.

**Deliverables:** lecturer inspection notes and real photograph.

## Step 9 — Upload and test on Arduino Uno (Answer 9)

- Use **Arduino IDE v2+** or a correctly configured Arduino toolchain. The current Step 9 heading specifies **Arduino Uno**, even though some stale table-of-contents/answer labels mention ESP32; follow the current Step 9 and verify any ambiguity with the lecturer.
- Connect the Arduino via USB to the computer.
- Identify the correct serial/COM port (on macOS, identify the corresponding `/dev/cu.*` port; on Windows, use Device Manager).
- Select the correct Arduino Uno board and port; if serial speed is configured, keep it at or below **115200 baud** as stated in the assessment.
- Create the final sketch named `XXX-InterRIoT-AT2-POR-Pt1.ino` with my initials.
- Copy the tested Tinkercad code into the Arduino sketch.
- Compile, upload and test the physical device.
- Verify that each press swaps LED states and that release does not affect them.
- Preserve final code for **Answer 9** and the compressed code project for submission.

**Acceptance test:** real Arduino behaves the same as the Tinkercad simulation.

## Step 10 — Record video evidence (Answer 10)

- Read **Appendix D: Video Recordings** in the original assessment before recording and follow its exact framing, content and format requirements.
- Ask me to record a short, clear video of the **actual physical circuit functioning**, showing the button and LED state changes.
- Verify that the recording visibly demonstrates initial state, button presses, LED swaps and release behaviour.
- **Do not paste anything into Answer 10**: the assessment explicitly instructs this.

**Deliverable:** separate real video file. Codex cannot produce authentic physical evidence without my recording.

## Step 11 — Submission (Answer 11 and Appendix A)

Prepare and verify **three separate submission items**:

1. Completed original assessment **Word document** containing all required written answers, screenshots, photographs and code in the explicitly requested Answer sections.
2. **Compressed Arduino IDE code project** (ZIP).
3. **Video evidence file** (not compressed).

Appendix A says not to compress Office documents, PDFs or videos; compress project code. Confirm the exact required filename for the Word document from the original appendix/lecturer. The assessment specifies **08:30 AM on the day of Session 5** as the due time; verify the actual calendar date with the lecturer. Do not substitute Appendix A's general 5 PM statement for the assessment-specific due time.

## Final quality checklist

- [ ] Correct circuit copied into Tinkercad and screenshot captured.
- [ ] Ohm's law and resistor calculations completed with assumptions.
- [ ] Five actual starter-code sections identified and explained.
- [ ] Flasher tested at 750 ms ON / 1500 ms OFF.
- [ ] Required `setLed`, `ledOn`, `ledOff` functions implemented.
- [ ] Press-and-hold ON/OFF behaviour tested.
- [ ] One-toggle-per-press behaviour tested.
- [ ] Second LED and resistor added; complementary states tested.
- [ ] Physical circuit checked by lecturer and photographed.
- [ ] Final code compiled, uploaded and tested on Arduino Uno.
- [ ] Real video recorded in accordance with Appendix D.
- [ ] Code style, comments, file headers and references completed.
- [ ] Three separate submission items prepared.

## First action for Codex

**Start with Step 1 only.** Ask me to provide the Tinkercad circuit diagram/starter circuit and confirm the semester, pin mappings, resistor values and button wiring. Then guide me through building and checking the simulation. Do not start coding Step 3 until Steps 1 and 2 are reviewed with me.
