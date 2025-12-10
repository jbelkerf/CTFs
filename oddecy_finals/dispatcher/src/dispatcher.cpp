#include "../inc/dispatcher.hpp"

std::string known_jobs[] = {"echo", "uname", "free", "add", "mysqldump"};

void create_job(std::vector<std::string> cmd, uint64_t time){
    // checking if the job exists
    unsigned long	i = 0;
    uint64_t		x = 0;
    while (i < (sizeof(known_jobs) / sizeof(known_jobs[0]))){
	if (cmd.front() == known_jobs[i])
	    break;
	i++;
    }
    // no job has been found
    if (i == (sizeof(known_jobs) / sizeof(known_jobs[0]))){
	logx.error("no job is matching <" + cmd.front() + ">");
	return;
    }

    for (auto it = cmd.begin() + 1; it != cmd.end(); it++){
	x += (*it).length() + 1;
    }

    // creating the job
    job *cjob = new job(time, cmd);
    cjob->general_purpose_buffer = new char[x + 1];
    memset(cjob->general_purpose_buffer, 0, x + 1);
    
    for (auto it = cmd.begin() + 1; it != cmd.end(); it++){
	strcat(cjob->general_purpose_buffer, (*it).c_str());
	// strcat(cjob->general_purpose_buffer, " ");
    }
    cjob->general_purpose_buffer[x - 1] = 0;

    jobs.push_back(cjob);
    
    std::thread cthread(&job::execute, cjob);
    cthread.detach();					// running in the background
    
}

void status_jobs(){
    logx.info("Current jobs");
    for (auto it = jobs.begin(); it != jobs.end(); it++){
	std::cout << "Job ID [" << (*it)->id  <<  "]\n"
	    << "\tJob time: " << (*it)->time << "\n"
	    << "\tTime Passed: " << (*it)->time_left  << "\n"
	    << "\tJob CMD: ";
	for (auto iti = (*it)->cmd.begin(); iti != (*it)->cmd.end(); iti++ ){
	    std::cout << *iti << " " ;
	}
	std::cout << std::endl;
    }
}

void stop_job(uint64_t idx){
    logx.info("deleting job number " + std::to_string(idx));
    for (auto it = jobs.begin(); it != jobs.end(); it++){
	if ((*it)->id == idx){
	    delete *it;
	    jobs.erase(it);
	    return;
	}
    }
}

void job::echo(){
    this->job_sleep();
    logx.info("job [" + std::to_string(this->id) + "]: ");
    puts(this->general_purpose_buffer);
}

void job::uname(){
    this->job_sleep();
    logx.info("job [" + std::to_string(this->id) + "]: ");
    std::cout << VERSION << std::endl;
}

void job::heap_stat(){
    this->job_sleep();
    logx.info("job [" + std::to_string(this->id) + "]: ");
    malloc_stats();
}

void job::mysqldump(char *dbtype){
    logx.info("job [" + std::to_string(this->id) + "]: ");
    logx.info("not implemented yet");
    (void) dbtype;
}

void job::job_sleep(){
    while (this->time_left < this->time){
	sleep(1);
	this->time_left++;
    }
}

void job::add(){
    this->job_sleep();
    logx.info("job [" + std::to_string(this->id) + "]: ");
    if (this->cmd.size() < 3){
	logx.error("less than two numerical arguments");
	return;
    }
    uint64_t a, b;
    a = atoll(cmd[1].c_str());
    b = atoll(cmd[2].c_str());
    // we dont wanna waste 8 bytes so just save it here
    *((uint64_t *)this->general_purpose_buffer) = a+b;
    std::cout << "Addition output : " << *((uint64_t *)this->general_purpose_buffer) << std::endl;
}

void job::execute(){
    if (this->cmd.front() == "echo"){
	this->echo();
    } else if (this->cmd.front() == "uname"){
	this->uname();
    } else if (this->cmd.front() == "free"){
	this->heap_stat();
    } else if (this->cmd.front() == "mysqldump"){
	this->job_sleep();
	this->mysqldump(this->general_purpose_buffer);
    } else if (this->cmd.front() == "add") {
	this->add();
    }

    std::cout << ">> " ;
    // search here for the current job in std::vector<jobs *> if we found it
    // delete it if not ign to not cause a double free
    if (std::find(jobs.begin(), jobs.end(), this) != jobs.end()) {
	jobs.erase(std::find(jobs.begin(), jobs.end(), this));
    }
}
