from odoo import models, fields, _, api


class OrderList(models.Model):
    _name = 'order.list'
    _description = "List Of Order"

    order_id = fields.Char()
    order_name = fields.Char()
    order_status = fields.Char()


class TrackingMailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.model
    def message_process(self, model, message, custom_values=None,
                        save_original=False, strip_attachments=False,
                        thread_id=None):
        res = super(TrackingMailThread, self).message_process(model, message, custom_values=None,
                                                        save_original=False, strip_attachments=False,
                                                        thread_id=None)
        data = str(message).split('Subject')[1]
        order_id = data.split(':')[1].split('/')[0]
        order_status = data.split(':')[2].split('\\n')[0]
        order_cost = data.split("Rs. ")[1].split(".")[0]
        order_code = data.split("Rs.")[0].split(" ")[-3]
        order_url = data.split('<')[1].split(">")[0].replace('\\n', '')
        order_note = data.replace('\\n', "").split('printable')[1].split('If you have any questions')[0]
        return res
