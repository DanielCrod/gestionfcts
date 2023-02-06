from odoo import fields, models, api


class alumno(models.Model):
    _name = "gestionfcts.alumno"
    _description = "descripción"

    name = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos", required=True)
    fecha = fields.Date("Fecha de nacimiento")
    foto = fields.Binary("Imagen")
    first_course = fields.Integer("Primer año de estudios", required=True)
    course = fields.Char(string="Curso académico")
    email = fields.Char("Email")
    telephone = fields.Integer("Teléfono de contacto")
    ciclo = fields.Selection([('0', 'DAM'), ('1', 'DAW'), ('2', 'ASIR'), ('3', 'SMR'), ('4', 'IC'), ('5', 'IO')],
                             "Ciclo formativo", default='0')
    work_period = fields.Selection([('0', 'Marzo'), ('1', 'Septiembre')], "Periodo de prácticas", default='0')
    dual = fields.Selection([('0', 'Si'), ('1', 'No')], "Dual", default='0')
    erasmus = fields.Selection([('0', 'Si'), ('1', 'No')], "Erasmus", default='0')
    empresa_id = fields.Many2one("gestionfcts.empresa", "Empresa", required=True, ondelete="cascade")


@api.depends('first_course', 'course')
def _course(self):
    for record in self:
        if len(str(record.first_course)) > 3:
            record.course = str(record.first_course) + "/" + str(record.first_course + 1)[2:]
        else:
            record.course = str(record.first_course) + "/" + str(record.first_course + 1)
