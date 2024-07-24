package word

import (
	"fmt"
)

func SearchWord() (findInfos []FindInfo) {
	word, files := getArgs()
	fileList := getFileList(files)
	cnt := len(fileList)

	ch := make(chan FindInfo)
	for _, filename := range fileList {
		go getFileInfo(word, filename, ch)
	}

	recvCnt := 0
	for findInfo := range ch {
		findInfos = append(findInfos, findInfo)
		recvCnt++
		if recvCnt == cnt {
			break
		}
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
