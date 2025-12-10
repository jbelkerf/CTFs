#ifndef DISPATCHER_HPP
#define DISPATCHER_HPP
#include "log.hpp"
#include <iostream>
#include <sstream>
#include <vector>
#include <malloc.h>
#include <string.h>
#include <thread>
#include <algorithm>
#include <iterator>
#include <stdint.h>

extern uint32_t pid;
extern std::string known_jobs[];

#define VERSION "Task manager v2.4"


class job {
    public :
	uint32_t			id = pid++;
	std::vector<std::string>	cmd;
	uint64_t			time = 0;
	uint64_t			time_left = 0;
	char				*general_purpose_buffer = NULL;


	void execute();
	void manage();
	void job_sleep();

	// jobs
	void echo();
	void uname();
	void heap_stat();
	virtual void mysqldump(char *dbtype);
	void add();

	job (uint64_t time, std::vector<std::string> cmd){
	    this->time = time;
	    this->time_left = 0;
	    this->cmd = cmd;
	}

	virtual ~job(){
	    delete general_purpose_buffer;
	}
};

void create_job(std::vector<std::string> cmd, uint64_t time);
void stop_job(uint64_t idx);
void status_job();
void status_jobs();


extern std::vector<job *> jobs;

#endif
