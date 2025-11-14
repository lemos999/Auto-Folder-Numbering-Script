import os
import re

def auto_number_folders(target_directory="."):
    """
    지정된 디렉토리 내의 폴더들에 자동으로 번호를 붙입니다.
    '숫자_' 접두사가 없는 폴더를 대상으로 합니다.
    """
    # 1. 디렉토리가 실제로 존재하는지 확인합니다.
    if not os.path.isdir(target_directory):
        print(f"오류: '{target_directory}'는 유효한 폴더 경로가 아닙니다.")
        return

    print(f"'{os.path.abspath(target_directory)}' 폴더를 스캔합니다...")

    # 2. 기존에 번호가 붙은 폴더들 중에서 가장 큰 숫자를 찾습니다.
    max_num = -1
    # 정규 표현식: 폴더 이름이 '숫자_'로 시작하는지 확인합니다.
    prefix_pattern = re.compile(r'^(\d+)_.*') 
    
    try:
        items = os.listdir(target_directory)
    except OSError as e:
        print(f"오류: 폴더를 읽는 중 문제가 발생했습니다. -> {e}")
        return

    for item_name in items:
        item_path = os.path.join(target_directory, item_name)
        if os.path.isdir(item_path): # 폴더인 경우에만 처리
            match = prefix_pattern.match(item_name)
            if match:
                num = int(match.group(1))
                if num > max_num:
                    max_num = num
    
    # 다음에 사용할 시작 번호
    next_num = max_num + 1
    print(f"현재 가장 큰 번호는 {max_num}입니다. {next_num}번부터 시작합니다.")

    # 3. 번호가 없는 폴더 목록을 만듭니다.
    folders_to_rename = []
    for item_name in items:
        item_path = os.path.join(target_directory, item_name)
        # 폴더이고, '숫자_' 접두사가 없는 경우
        if os.path.isdir(item_path) and not prefix_pattern.match(item_name):
            folders_to_rename.append(item_name)
            
    # 4. 가나다순으로 정렬하여 일관성을 유지합니다.
    folders_to_rename.sort()

    if not folders_to_rename:
        print("번호를 붙일 새로운 폴더가 없습니다.")
        return

    print("\n아래 폴더들의 이름을 변경합니다:")
    for folder_name in folders_to_rename:
        print(f"- {folder_name}")

    # 5. 실제로 폴더 이름을 변경합니다.
    print("\n--- 작업 시작 ---")
    for folder_name in folders_to_rename:
        old_path = os.path.join(target_directory, folder_name)
        new_name = f"{next_num}_{folder_name}"
        new_path = os.path.join(target_directory, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"성공: '{folder_name}' -> '{new_name}'")
            next_num += 1
        except OSError as e:
            print(f"실패: '{folder_name}' 이름 변경 중 오류 발생 -> {e}")

    print("--- 작업 완료 ---")


# --- 스크립트 사용 방법 ---
if __name__ == "__main__":
    # 이 스크립트는 실행된 위치(경로)에 있는 폴더들에 자동으로 번호를 붙입니다.
    # 따라서 스크립트 내에서 경로를 직접 수정할 필요가 없습니다.
    print("스크립트가 실행된 폴더를 대상으로 자동 번호매기기를 시작합니다.")
    auto_number_folders()
