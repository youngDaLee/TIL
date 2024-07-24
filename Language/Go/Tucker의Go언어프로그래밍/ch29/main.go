package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sort"
	"strconv"

	"gopkg.in/DataDog/dd-trace-go.v1/contrib/gorilla/mux"
)

type Student struct {
	Id    int
	Name  string
	Age   int
	Score int
}

var students map[int]Student
var lastId int

type Students []Student

func (s Students) Len() int {
	return len(s)
}
func (s Students) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}
func (s Students) Less(i, j int) bool {
	return s[i].Id < s[j].Id
}

func MakeWebHandler() http.Handler {
	mux := mux.NewRouter()
	// barHandler 이용 parma
	mux.HandleFunc("/search", barHander)
	// func
	mux.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "Hello Bar")
	})
	// static 접근
	mux.Handle("/", http.FileServer(http.Dir("static")))
	mux.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
	// json 리턴
	mux.HandleFunc("/student", StudentHander)

	// REST API
	mux.HandleFunc("/students", GetStudentListHander).Methods("GET")

	return mux
}

func barHander(w http.ResponseWriter, r *http.Request) {
	values := r.URL.Query()
	name := values.Get("name")
	if name == "" {
		name = "World"
	}
	id, _ := strconv.Atoi(values.Get("id"))
	fmt.Fprintf(w, "Hello %s! id:%d", name, id)
}

func StudentHander(w http.ResponseWriter, r *http.Request) {
	student := Student{1, "aaa", 16, 87}
	data, _ := json.Marshal(student)
	w.Header().Add("content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, string(data))
}

func GetStudentListHander(w http.ResponseWriter, r *http.Request) {
	students = make(map[int]Student)
	students[1] = Student{1, "aaa", 16, 87}
	students[2] = Student{2, "bbb", 18, 57}
	lastId = 2

	list := make(Students, 0)
	for _, student := range students {
		list = append(list, student)
	}
	sort.Sort(list)

	w.Header().Add("content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(list)
}

func main() {
	http.ListenAndServe(":3000", MakeWebHandler()) // 웹 서버 시작
}
