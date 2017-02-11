#!/bin/bash

more small_access_log_Jul95_01.txt | python fltr_wlog_trbts.py
more small_access_log_Jul95_01.txt | python fltr_wlog_ip_trbts_toops.py
more small_access_log_Jul95_01.txt | python fltr_wlog_status_codes.py 200
more small_access_log_Jul95_01.txt | python fltr_wlog_status_codes.py 200 | python count_lines.py
more small_access_log_Jul95_01.txt | python fltr_wlog_status_codes.py 200 | python top_n.py 2
more small_access_log_Jul95_01.txt | python fltr_wlog_ip_trbts_toops.py | python dsc_sort_ip_trbts_toops.py
more small_access_log_Jul95_01.txt | python fltr_wlog_ip_trbts_toops.py | python dsc_sort_ip_trbts_toops.py

#more small_access_log_Jul95_01.txt | python fltr_wlog_ip_trbts_toops.py | python dsc_sort_ip_trbts_toops.py | python stdin_encrypt.py



exit
