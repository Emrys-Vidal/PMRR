import sys
import os
import pdfplumber


# Only find checkboxes this size
RECT_WIDTH = 9.3
RECT_HEIGHT = 9.3
RECT_TOLERANCE = 2

# Each stroke of the 'x' has the same bounding box
# as the checkbox (approximately)
CHECKBOX_X_WIDTH = RECT_WIDTH
CHECKBOX_X_HEIGHT = RECT_HEIGHT
CHECKBOX_X_TOLERANCE = RECT_TOLERANCE


def print_item(item):
    return "x0=%s x1=%s y0=%s y1=%s" % ( item['x0'], item['x1'], item['y0'], item['y1'] )

def filter_rects(rects):
    ## Just get the rects that are the right size to be checkboxes
    rects_found = []
    for rect in rects:
        if ( rect['height'] > ( RECT_HEIGHT - RECT_TOLERANCE )   
            and ( rect['height'] < RECT_HEIGHT + RECT_TOLERANCE) 
            and ( rect['width'] < RECT_WIDTH + RECT_TOLERANCE) 
            and ( rect['width'] < RECT_WIDTH + RECT_TOLERANCE) ):
            rects_found.append(rect)
            #print rect
    return rects_found

def determine_if_checked(checkbox, curve_list):
    # This figures out if the bounding box of (either) line used to make
    # one half of the 'x' is the right size and overlaps with a rectangle.
    # This isn't foolproof, but works for this case. 
    # It's not totally clear (to me) how common this style of checkboxes
    # are used, and whether this is useful approach to them.
    # Also note there should be *two* matching LTCurves for each checkbox.
    # But here we only test there's at least one. 


    for curve in curve_list:


        if ( checkbox['height'] > ( CHECKBOX_X_HEIGHT- CHECKBOX_X_TOLERANCE )   
            and ( checkbox['height'] < CHECKBOX_X_HEIGHT + CHECKBOX_X_TOLERANCE) 
            and ( checkbox['width'] < CHECKBOX_X_WIDTH + CHECKBOX_X_TOLERANCE) 
            and ( checkbox['width'] < CHECKBOX_X_WIDTH + CHECKBOX_X_TOLERANCE) ):

            xmatch = False
            ymatch = False

            if ( max(checkbox['x0'], curve['x0']) <= min(checkbox['x1'], curve['x1']) ):
                xmatch = True
            if ( max(checkbox['y0'], curve['y0']) <= min(checkbox['y1'], curve['y1']) ):
                ymatch = True
            if xmatch and ymatch:
                #print "Found %s inside %s \n\n" % (print_item(curve), print_item(checkbox))
                return True

    return False




def get_checkboxes_from_file(filepath):
    # get a pdfplumber obj for them:
    this_pdf =  pdfplumber.open(filepath)
    p0 = this_pdf.pages[0]
    
    try:
        curves = p0.objects["curve"]
        rects = p0.objects["rect"]
    except KeyError:
        return None
    
    rects = filter_rects(rects)
    # for each checkbox we found figure out if it is checked.
    for i, rect in enumerate(rects): 
        result = determine_if_checked(rect, curves)
        rects[i]['checked'] = result


    print "found %s rects and %s curves" % (len(rects), len(curves))
    return rects


if __name__ == "__main__":


    ROOT_PATH = "/dir/where/there/are/pdfs/"
    count = 0
    for dirName, subdirList, fileList in os.walk(ROOT_PATH):
        print('Found directory: %s' % dirName)
        for fileName in fileList:

            if fileName.find('.pdf') > 0:
                count += 1

                print('\tHandling %s - %s  %s' % (count, dirName, fileName))
                filepath = dirName + "/" + fileName

                checkboxes = get_checkboxes_from_file(filepath)
                true_count = sum(1 for x in checkboxes if x['checked'])
                print " %s are checked" % (true_count)


    print "TOTAL OF %s PROCESSED" % count 



