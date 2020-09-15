# Ansible iCal lookup plugin

This Ansible lookup plugin verifies if a specific date (ISO8601) matches with 
an event in an iCal calendar.

Currently retrieves an url based iCal.


## Usage

lookup('ical', instant) 

```Example:
   - name: Test with time = "{{ instant }}"
      debug:
        msg: "There's an event now:"
      when: "{{ lookup('ical', url, instant=instant) }}"
      vars:
        instant: "{{ lookup('pipe','date -u +%Y-%m-%dT%H:%M:%S%z') }}"
```

##ToDo
validate with local ical files. 
