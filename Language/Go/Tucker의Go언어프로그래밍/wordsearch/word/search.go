package word

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

type FindInfo struct {
	filename string
	lines    []LineInfo
}
type LineInfo struct {
	lineNo int
	line   string
}

// 실행 파라미터로부터 찾는 단어, 파일명을 가져오는 함수
func getArgs() (word string, files []string) {
	if len(os.Args) < 3 {
		panic("2개 이상의 실행 인수가 필요합니다")
	}

	word = os.Args[1]
	files = os.Args[2:]
	return
}

// 읽을 파일 리스트
func getFileList(paths []string) (filelist []string) {
	for _, path := range paths {
		files, err := filepath.Glob(path)
		if err != nil || files == nil {
			fmt.Println("파일 경로가 잘못되었습니다 path: ", path)
			panic("panic! 종료..")
		}
		filelist = append(filelist, files...)
	}
	return
}

// 파일 읽고 찾은 정보 리턴
func getFileInfo(word, filename string) (findInfo FindInfo) {
	findInfo.filename = filename
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("파일을 읽을 수 없습니다 filename: ", filename)
		panic("panic! 종료..")
	}
	defer file.Close() // 함수 종료 전 파일 닫기

	lineNo := 1
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, word) {
			findInfo.lines = append(findInfo.lines, LineInfo{lineNo, line})
		}
		lineNo++
	}
	return
}

func SearchWord() (findInfos []FindInfo) {
	word, files := getArgs()
	fileList := getFileList(files)

	for _, filename := range fileList {
		findInfos = append(findInfos, getFileInfo(word, filename))
	}
	return
}

func PrintSearchWord(findInfos []FindInfo) {
	for _, findInfo := range findInfos {
		fmt.Println(findInfo.filename)
		fmt.Println("-----------------------------------")
		for _, lineInfo := range findInfo.lines {
			fmt.Printf("\t%d\t%s\n", lineInfo.lineNo, lineInfo.line)
		}
		fmt.Println("-----------------------------------")
		fmt.Println()
	}
}
