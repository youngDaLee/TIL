package main

import (
	"flag"
	"os"
	"runtime"
	"time"

	"github.com/davecgh/go-spew/spew"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
)

// 커멘드라인 플래그 - 커멘드라인 프로그램에서 옵션을 지정하는 방법
func ex60() {
	envPtr := flag.String("env", "prod", "환경변수")
	cpuPtr := flag.Int("cpu", runtime.NumCPU(), "CPU수")
	flag.Parse() // 플래그값 읽기 위해 필요
	spew.Dump(envPtr)
	spew.Dump(cpuPtr)
}

// 로깅
func ex61() {
	envPtr := flag.String("env", "prod", "환경변수")
	cpuPtr := flag.Int("cpu", runtime.NumCPU(), "CPU수")
	flag.Parse() // 플래그값 읽기 위해 필요

	if *envPtr != "prod" {
		log.Logger = log.Output(zerolog.ConsoleWriter{
			Out:        os.Stdout,
			TimeFormat: time.RFC3339,
		})
	}
	log.Info().Str("env", *envPtr).Int("cpu", *cpuPtr).Msg("프로그램이 시작되었습니다")
}

// GoDoc 고독.... 고독....고독... 고 문서화 프로그램..고독한 문서화 프로그램...
/*
이렇게 상위에 문서화 하고
*/
// 메서드 위에 주석 달아서 문서화해줌...
func ex62() {
}

// 몌ㅑ
func main() {
	ex61()
}
