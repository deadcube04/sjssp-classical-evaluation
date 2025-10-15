best = {
        "jobs" : {
            "job_1" : [([1],[1],1), ([1],[2],1)],
            "job_2" : [([2],[1],1), ([2],[2],1)],
        },
        "machine_downtimes" : {},
        "timespan": 3
        }

medium =  {
        "jobs" : {
            "job_1" : [([1],[],1)],
            "job_2" : [([2],[],1)]
        },
        "machine_downtimes" : {},
        "timespan": 2
        }

worst =  {
        "jobs" : {
            "job_1" : [([1],[],1)],
            "job_2" : [([1],[],1)]
        },
        "machine_downtimes" : {},
        "timespan": 2
        }

insane = {
        "jobs" : {
            "job_1" : [([1, 3],[],1), ([1,3],[],1)],
            "job_2" : [([2, 3],[],1), ([2,3],[],1)],
            "job_3" : [([2, 3],[],1), ([2,3],[],1)],
            "job_4" : [([1, 2, 3],[],2), ([1,2,3],[],2)],
            "job_5" : [([1],[],3), ([1],[],3)],
       
        },
        "machine_downtimes" : {},
        "timespan": 10
        }