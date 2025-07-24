best = {
        "jobs" : {
            "job_1" : [([1, 2],[],1)],
            "job_2" : [([1, 2],[],1)],
        },
        "machine_downtimes" : {},
        "timespan": 2
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
            "job_1" : [([1, 3],[],1)],
            "job_2" : [([2, 3],[],1)],
            "job_3" : [([2, 3],[],1)],
            "job_4" : [([1, 2, 3],[],2)],
            "job_5" : [([1],[],3)],
            "job_6" : [([1],[],2)],
            "job_7" : [([1],[],4)],
            "job_8" : [([1],[],1)],    
            "job_9" : [([2],[],10)],
            "job_10": [([3],[],1)],
        },
        "machine_downtimes" : {},
        "timespan": 10
        }