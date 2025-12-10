#include "../inc/dispatcher.hpp"

ws_logx logx;
std::vector<job *> jobs;
uint32_t pid = 0;

std::vector<std::string> split_cmd(std::string &cmd){
    std::vector<std::string> spl_cmd;
    std::stringstream scmd(cmd);
    std::string item;
    while (std::getline(scmd, item, ' ')) {
	if (item.length() > 0){
	    spl_cmd.push_back(item);
	}
    }
    return spl_cmd;
}

void help(){
    logx.info("todo - write the help");
}

void dispatch_menu(){
    std::vector<std::string> cmd;
    std::string p;
    while (true){
	std::cout << ">> " ;
	// getting user input
	std::getline(std::cin, p);
	cmd = split_cmd(p);
	if (cmd.size() < 1)
	    continue ;
	// treating the user input
	if (cmd.front() == "HELP") {
	    help();
	    continue ;
	} else if (cmd.front() == "RUN" ){
	    if (cmd.size() < 3)
		continue;
	    uint64_t cmdtime;
	    try {
		cmdtime = std::stoi(cmd[1]);
		cmd.erase(cmd.begin(), cmd.begin() + 2); 
	    } catch (...) {
		logx.warn("CMD time is not provided or invalid, replacing with default (10s)");
		cmdtime = 10;
		cmd.erase(cmd.begin(), cmd.begin() + 1); 
	    }
	    create_job(cmd, cmdtime);
	} else if (cmd.front() == "REMOVE"){
	    if (cmd.size() != 2){
		logx.info("REMOVE accepts only one numerical argument");
		continue;
	    }
	    uint64_t idx;
	    try {
		idx = std::stoi(cmd[1]);
	    } catch (...) {
		logx.error("REMOVE accepts a numerical argument");
		continue;
	    }
	    stop_job(idx);
	} else if (cmd.front() == "JOBS"){
	    status_jobs();
	}
    }
}

void ignore_me(){
    // ignore me 
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    setvbuf(stderr, 0, _IONBF, 0);
    // ignore me 
}

int main() {
    ignore_me();
    logx.info("TASK MANAGER v2.4");
    dispatch_menu();
}
