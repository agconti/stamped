from django import template
import datetime
import pytz # for time zone handleing 

register = template.Library()

@register.tag(name="timePosted")
def do_time_since(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, date_to_format = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return TimePostedNode(date_to_format)

class TimePostedNode(template.Node):
    def __init__(self, date_to_format):
        self.date_to_format = template.Variable(date_to_format)
    def render(self, context):
        try:
            d = self.date_to_format.resolve(context)
            delta = datetime.datetime.now(pytz.utc) - d
            if delta.days > 7:
                return "Posted %s days ago." %(delta.days)
            elif delta.seconds//3600 > 1:
                return "Posted %s days and %s minutes ago." %(delta.days, delta.seconds//3600)
            else:
                 return "Posted %s seconds ago." %((delta.seconds//60)%60)
        except template.VariableDoesNotExist:
            return ''

@register.tag(name="pctChange")
def do_pctChange(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, args = token.split_contents()
        end, begin = args.split()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires that arguments are in quotes" % token.contents.split()[0])
    #slice to remove quotes
    return pctChangeNode(end[1:], begin[:-1])

class pctChangeNode(template.Node):
    def __init__(self, end, begin):
        self.begin = template.Variable(begin)
        self.end = template.Variable(end)
    def render(self, context):
        try:
            begin = self.begin.resolve(context)
            end = self.end.resolve(context)
            return "%0.2f%%" %(((end - begin)/ float(begin)) * 100)
        except template.VariableDoesNotExist:
            return ''