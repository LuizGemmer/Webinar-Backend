from rest_framework import serializers

class UserFunctionReviewsDoneOnYearSerializer(serializers.Serializer):
    # return values
    apt = serializers.IntegerField(read_only=True)
    pending = serializers.IntegerField(read_only=True)
    obsolete = serializers.IntegerField(read_only=True)

    # filters
    functions = serializers.ListField(write_only=True)
    subsectors = serializers.ListField(write_only=True)
    sectors = serializers.ListField(write_only=True)
