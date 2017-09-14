class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_call, reason_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_call = time_call
        self.reason_call = reason_call

    def display(self):
        print 'Unique_id: ' + str(self.unique_id)
        print 'Callers name is: ' + str(self.caller_name)
        print 'Callers phone # is: ' + str(self.caller_phone_number)
        print 'Time of call is: ' + str(self.time_call)
        print 'Reason for call is: ' + str(self.reason_call)

    def __repr__(self):
        return "<Call Object: {}>".format(self.call_phone_number)

call1 = Call(1, 'Ken', 2066268009, 1145, 'missing package')
call2 = Call(2, "Daniel", 2066268033, 1150, "damaged package")
call3 = Call(3, "Indhu", 2066268031, 1155, "praise and joy")
call1.display()
call2.display()
call3.display()

class CallCenter(object):
    def __init__(self):
        self.calls = []

    @property
    def queue_size(self):
        return len(self.calls)

    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self):
        self.queue_size -=1
        return self

    def info(self):
        print self.caller_name
        print self.caller_phone_number
        print self.queue_size
        return self

center = CallCenter()
center.add(call1).add(call2).add(call3)
print center.queue_size