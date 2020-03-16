from ..models.empty_forms import EmptyForms
from ..models.empty_forms_imgs import EmptyFormsImgs
from ..models.filled_forms import FilledForms
from ..models.filled_forms_imgs import FilledFormsImgs


def get_all_forms() -> list:
    return EmptyForms.objects.all()


def get_all_client_forms(client_id: str) -> list:
    """
    Retrieve a list of forms for a given client
    :param client_id: String representing the client Object ID
    :return: list - EmptyForms
    """
    return EmptyForms.objects.filter(client_id=client_id)


def get_empty_form(form_id: str) -> EmptyForms:
    """
    Retrieves the empty form for the given form ID
    :param form_id: ID of the form to be retrieved
    :return: EmptyForms
    """
    return EmptyForms.objects(_id=form_id).first()


def augment_forms_with_images(forms: list, func: callable) -> list:
    """
    Augment the given list of forms with the image data for each page
    :param forms:
    :param func:
    :return:
    """
    if callable(func):
        # Get the list of image IDs
        pages = []
        for item in forms:
            for page in item.pages.values():
                pages.append(page)
        image_ids = list(map(lambda page_item: page_item['image'], pages))

        # Get the list of images given the image IDs
        images = func(image_ids)
        image_dict = {image.id: image for image in images}

        # Augment forms with images for each page
        for form in forms:
            for page in form.pages.values():
                if page['image'] in image_dict:
                    page['image'] = image_dict[page['image']]['image'].decode('ascii')

    return forms


def get_empty_form_images(image_ids: list) -> list:
    """
    Retrieve empty form images for the list of image ids provided
    :param image_ids: list of image IDs (UUID4 converted to a string)
    :return: list - EmptyFormsImages
    """
    return EmptyFormsImgs.objects.filter(_id__in=image_ids)


def get_filled_forms(form_id: str) -> list:
    """
    Retrieves all filled forms for the given form ID
    :param form_id: The empty form ID the filled forms are related to
    :return: list - FilledForms
    """
    return FilledForms.objects.filter(form_id=form_id).all()


def get_filled_form_images(image_ids: list) -> list:
    """
    Retrieve empty form images for the list of image ids provided
    :param image_ids: list of image IDs (UUID4 converted to a string)
    :return: list - EmptyFormsImages
    """
    return FilledFormsImgs.objects.filter(_id__in=image_ids)
