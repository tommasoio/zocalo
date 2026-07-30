import csv


class CsvExporter:

    def export(self, polls, filename):

        with open(

            filename,

            "w",

            newline="",

            encoding="utf8"

        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                "Question",

                "Votes"

            ])

            for poll in polls:

                writer.writerow([

                    poll["question"],

                    len(poll["votes"])

                ])
