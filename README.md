# Auto Folder Numbering Script

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple Python script that automatically adds numerical prefixes (e.g., `01_`, `02_`) to folders within a directory. This is particularly useful for improving file system performance on traditional Hard Disk Drives (HDDs).

**[Table of Contents]**
1.  [English Documentation](#english-documentation)
2.  [Korean Documentation (한국어 문서)](#korean-documentation-한국어-문서)
3.  [License](#license)

---

## **English Documentation**

### **Motivation**

On traditional Hard Disk Drives (HDDs), the physical location of data matters. When a directory contains many folders, the file system needs to read the metadata for each one. If the folder names are not in a logical order, the HDD's read/write head has to jump around the disk platter to find the data, increasing seek time and slowing down directory listing.

This script solves the problem by enforcing a numerical order. By prefixing folder names with `01_`, `02_`, etc., it ensures they are stored and indexed in a sequential, predictable manner, which can lead to faster directory access on HDDs.

### **Features**

*   **Automatic Numbering:** Scans the target directory and finds the highest existing number to continue from.
*   **Consistent Ordering:** Sorts un-prefixed folders alphabetically before numbering to ensure a consistent and predictable result every time.
*   **Safe Execution:** Only affects folders that do not already have a numerical prefix.
*   **Portability:** Can be run directly if Python is installed, or compiled into a single `.exe` for use on any Windows machine.

### **How It Works**

The script follows a clear, step-by-step logic:

1.  **Find the Starting Number:** It first scans all items in the directory to find folders that already have a `number_` prefix. It identifies the highest number used and sets the starting point for new folders to be `highest_number + 1`.
2.  **Identify Folders to Rename:** The script then iterates through the directory again to find all folders that do *not* have a numerical prefix. These are collected into a list.
3.  **Sort for Consistency:** To ensure the numbering order is always the same, this list of target folders is sorted alphabetically.
4.  **Apply New Names:** Finally, the script loops through the sorted list, renaming each folder by adding the sequential number prefix (e.g., `folder_A` becomes `15_folder_A`).

### **Usage**

There are two ways to use this script:

#### **Method 1: Direct Execution (Requires Python)**

1.  **Prerequisites:** Ensure you have Python installed on your system.
2.  **Preparation:** Place the `a.py` script **inside the directory** where you want to number the folders.
3.  **Execution:** Open a terminal (Command Prompt, PowerShell, etc.) in that directory and run the command:
    ```bash
    python a.py
    ```

#### **Method 2: Using the Compiled Executable (.exe)**

This method is for Windows users and does not require Python to be installed on the target machine.

1.  **How to Compile (Developer Step):**
    *   First, install PyInstaller on a machine that has Python:
        ```bash
        pip install pyinstaller
        ```
    *   Navigate to the script's directory and run the following command to create a single executable file:
        ```bash
        pyinstaller --onefile a.py
        ```2.  **How to Use the `.exe` File:**
    *   Find the `a.exe` file inside the `dist` folder created by PyInstaller.
    *   Copy `a.exe` **into the directory** containing the folders you want to number.
    *   Double-click `a.exe` to run it. The folders will be numbered automatically.

---

## **Korean Documentation (한국어 문서)**

### **개발 동기**

전통적인 HDD(하드 디스크 드라이브)는 데이터의 물리적 위치가 성능에 영향을 줍니다. 하나의 디렉토리 안에 많은 폴더가 있을 경우, 파일 시스템은 각 폴더의 메타데이터를 읽어야 합니다. 만약 폴더 이름이 논리적인 순서 없이 흩어져 있다면, HDD의 헤드는 디스크 플래터를 오가며 데이터를 찾아야 하므로 탐색 시간이 길어지고 폴더를 불러오는 속도가 느려집니다.

이 스크립트는 폴더 이름 앞에 `01_`, `02_` 와 같은 숫자 접두사를 붙여 강제적으로 순서를 부여함으로써 이 문제를 해결합니다. 이를 통해 폴더가 순차적으로 예측 가능하게 저장 및 인덱싱되도록 보장하며, 결과적으로 HDD 환경에서 더 빠른 디렉토리 접근 속도를 기대할 수 있습니다.

### **주요 기능**

*   **자동 번호 부여:** 대상 디렉토리를 스캔하여 이미 존재하는 가장 큰 번호를 찾아내고, 그 다음 번호부터 순차적으로 부여합니다.
*   **일관된 정렬:** 번호가 없는 폴더들을 가나다순으로 먼저 정렬한 후 번호를 부여하여, 스크립트를 여러 번 실행해도 항상 동일하고 예측 가능한 결과를 보장합니다.
*   **안전한 실행:** 이미 `숫자_` 접두사가 있는 폴더는 건드리지 않고, 접두사가 없는 폴더에만 작업을 수행합니다.
*   **높은 이식성:** Python이 설치된 환경에서는 직접 실행할 수 있으며, `.exe` 파일로 컴파일하여 Python이 없는 Windows PC에서도 사용할 수 있습니다.

### **작동 원리**

스크립트는 명확한 단계별 로직을 따릅니다.

1.  **시작 번호 찾기:** 먼저 디렉토리 내의 모든 항목을 스캔하여 `숫자_` 접두사가 붙은 폴더를 찾습니다. 그중 가장 큰 번호를 확인하고, 새로 번호를 붙일 시작점을 `가장 큰 번호 + 1`로 설정합니다.
2.  **이름을 변경할 폴더 식별:** 스크립트가 디렉토리를 다시 스캔하여 숫자 접두사가 *없는* 모든 폴더를 찾아 목록으로 만듭니다.
3.  **일관성을 위한 정렬:** 번호 부여 순서가 항상 동일하도록, 위 단계에서 만든 폴더 목록을 가나다순으로 정렬합니다.
4.  **새 이름 적용:** 마지막으로, 정렬된 목록을 순회하며 각 폴더 이름 앞에 순차적인 번호 접두사를 붙여 이름을 변경합니다. (예: `폴더A` -> `15_폴더A`)

### **사용 방법**

스크립트를 사용하는 방법은 두 가지입니다.

#### **방법 1: 직접 실행 (Python 필요)**

1.  **준비물:** 시스템에 Python이 설치되어 있어야 합니다.
2.  **준비:** `a.py` 스크립트 파일을 **번호를 부여하려는 폴더들이 있는 디렉토리 안으로** 복사합니다.
3.  **실행:** 해당 디렉토리에서 터미널(명령 프롬프트, PowerShell 등)을 열고 아래 명령어를 입력합니다.
    ```bash
    python a.py
    ```

#### **방법 2: 컴파일된 실행 파일(.exe) 사용**

이 방법은 Windows 사용자를 위한 것이며, 스크립트를 사용할 PC에 Python이 설치되어 있지 않아도 됩니다.

1.  **컴파일 방법 (개발자용):**
    *   먼저, Python이 설치된 PC에서 PyInstaller를 설치합니다.
        ```bash
        pip install pyinstaller
        ```
    *   스크립트가 있는 디렉토리로 이동한 후, 아래 명령어를 실행하여 단일 실행 파일을 생성합니다.
        ```bash
        pyinstaller --onefile a.py
        ```
2.  **`.exe` 파일 사용법:**
    *   PyInstaller가 생성한 `dist` 폴더 안에서 `a.exe` 파일을 찾습니다.
    *   이 `a.exe` 파일을 **번호를 부여하려는 폴더들이 있는 디렉토리 안으로** 복사합니다.
    *   `a.exe` 파일을 더블클릭하여 실행하면 폴더에 자동으로 번호가 부여됩니다.
