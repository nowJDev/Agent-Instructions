# 업무보고의 줄 수·구조·명시적 문체 패턴만 읽기 전용으로 검사한다.
import argparse
from datetime import date
from pathlib import Path
import re
import sys


# shortcut: 명확한 종결형만 탐지하며 한국어 의미·명사형 전체 판정은 에이전트가 원본과 대조한다.
FINITE_ENDING = re.compile(
    r'(?:했다|한다|하였습니다|했습니다|했음|하였음|하고 있습니다|할 예정입니다|'
    r'(?:구현|적용|반영|개선|수정|보정|검토|분석|설계|수립|작성|검증|완료|정리|연동|배포|확인|수행|실행|테스트)함)[.!。]?\s*$')
DECORATION = re.compile(r'^\s*(?:#{1,6}\s|`{3,}|~{3,}|>|\||[-*+]\s+\[[ xX]\]|:?-+:?\s*\|)|\*\*|(?<!\w)__\S.*\S__(?!\w)|`')


def validate_report(text, mode='default', min_lines=None, max_lines=None, expected_heading=None):
    """Return mechanical errors; this does not verify source truth or completion."""
    errors = []
    text = text.removeprefix('\ufeff')
    lines = text.splitlines()
    low = (10 if mode == 'default' else 1) if min_lines is None else min_lines
    high = (12 if mode == 'default' else None) if max_lines is None else max_lines
    if len(lines) < low or (high is not None and len(lines) > high):
        errors.append(f'줄 수 {len(lines)}: 허용 범위 {low}~{high if high is not None else "제한 없음"}')
    for number, line in enumerate(lines, 1):
        if not line.strip():
            errors.append(f'{number}행: 공백 행 금지')
        if line != line.rstrip():
            errors.append(f'{number}행: 끝 공백 금지')
        if DECORATION.search(line):
            errors.append(f'{number}행: 표 또는 Markdown 장식 금지')
        if FINITE_ENDING.search(line):
            errors.append(f'{number}행: 명시적 서술형 종결 탐지')
        if '\ufffd' in line or any(ord(char) < 32 for char in line):
            errors.append(f'{number}행: 손상 문자 또는 제어 문자 탐지')
    if expected_heading is not None:
        candidates = [lines[2].strip()] if mode == 'default' and len(lines) > 2 else [line.strip() for line in lines]
        if expected_heading not in candidates:
            errors.append('업무 헤더: 사용자 지정 문자열과 정확히 일치하지 않음')
    if mode == 'default':
        match = re.fullmatch(r'\((\d{1,2})/(\d{1,2})\) 일일 업무', lines[0]) if lines else None
        try:
            if match is None:
                raise ValueError
            date(2000, int(match[1]), int(match[2]))
        except ValueError:
            errors.append('날짜: (M/D) 일일 업무 형식 또는 월·일 오류')
        if len(lines) < 2 or lines[1] != '1. 주요 업무내용':
            errors.append('2행: 1. 주요 업무내용 필요')
        if len(lines) < 3 or not re.fullmatch(r'  \d+\.\d+ \S.*', lines[2]):
            errors.append('3행: 두 칸 들여쓴 대상 업무 번호·제목 필요')
        if len(lines) < 4 or not re.fullmatch(r'    - \S.*', lines[3]):
            errors.append('4행: 네 칸 들여쓴 상위 요약 1개 필요')
        details = lines[4:]
        if not 6 <= len(details) <= 8 or any(not re.fullmatch(r'      = \S.*', line) for line in details):
            errors.append('세부 구조: 여섯 칸 들여쓴 = 항목 6~8개 필요')
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description='보고서 형식 검사. UTF-8/BOM 허용. 빈행은 금지하며 끝 개행 0~1개 허용. 사실 검증은 별도 수행.')
    parser.add_argument('--input', required=True, help='보고서 경로. - 는 UTF-8 표준입력')
    parser.add_argument('--mode', choices=('default', 'custom'), default='default')
    parser.add_argument('--min-lines', type=int)
    parser.add_argument('--max-lines', type=int)
    parser.add_argument('--expected-heading', help='앞 들여쓰기를 제외한 정확한 업무 헤더')
    args = parser.parse_args(argv)
    low = (10 if args.mode == 'default' else 1) if args.min_lines is None else args.min_lines
    high = (12 if args.mode == 'default' else None) if args.max_lines is None else args.max_lines
    if low < 1 or (high is not None and high < low):
        parser.error('줄 수 범위는 1 이상이며 min-lines <= max-lines여야 함')
    try:
        text = (sys.stdin.buffer.read().decode('utf-8-sig') if args.input == '-'
                else Path(args.input).read_text(encoding='utf-8-sig'))
    except (OSError, UnicodeError) as exc:
        print(f'ERROR: 입력 읽기 실패: {exc}', file=sys.stderr)
        return 2
    errors = validate_report(text, args.mode, args.min_lines, args.max_lines, args.expected_heading)
    if errors:
        print('\n'.join('FAIL: ' + error for error in errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(text.removeprefix(chr(0xfeff)).splitlines())}행, mode={args.mode} (형식 검사만 수행)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
